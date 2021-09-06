import os
if not os.name == 'nt':
    raise ImportError("You must be on Windows OS to use this packages")
# Only usable on Windows OS
import d3dshot
from SimConnect import *
# Only usable on Windows OS
from PySide2.QtCore import QObject, SIGNAL, Signal, Slot   
import cv2
import time
import imutils
import sys
import numpy as np
import cv2 as cv
import config.configs as config

class Recorder(QObject):
    progress = Signal(int)
    finished = Signal()


    def __init__(
        self, 
        root, 
        folder_name,
        d3d , 
        number_images, 
        image_format, 
        fps = 1.0,
        vars = config.VARS,
        vars_be= config.VARS_BEGIN_END,
        units= config.UNITS,
        units_be= config.UNITS_BEGIN_END
    ):
        super(Recorder,self).__init__()
        self.root = root
        self.d = d3d
        self.folder_name = folder_name
        self.number_images = number_images
        self.image_format = image_format
        self.fps = fps
        self.vars = vars
        self.vars_be = vars_be
        self.units = units
        self.units_be = units_be
        self.pause = 1 / fps  # time in sec
        os.makedirs(self.root+'/'+folder_name, exist_ok=True)

class Msfs_recorder(Recorder):
    """
    Class that records :
        - Images (tested on 4K >= images)
        - MSFS2020 Simvars (such as attitude)
    \n
    TODO:
    * Find a way to record at constant delta with right corresponding values \n
    For now Only starting/ending values could be a good way to solve some issues but at cost of precision
    As is for now (delta is too large)
    """
    def set_d3d(self,d3d):
        self.d = d3d
    def run(self):
        """
        Runs the recording
        """
        # initialize sim connect
        sm = SimConnect()
        aq = AircraftRequests(sm, _time=0)

        # initialize outputs
        f = open(self.root+'/'+self.folder_name + "/values.txt", "w")
        f_i = open(self.root+'/'+self.folder_name + "/images.txt", "w")

        # initialize d3d capture
        self.d

        try:
            # save attitude / heading at begining
            sim_units = self.units
            sim_units_end = self.units_be
            sim_vars = self.vars
            sim_vars_end = self.vars_be

            # file footer and header 's inforamtion
            header_number_images = (
                "# NUMBER OF IMAGES\n" + str(self.number_images) + "\n"
            )
            header_str = "# UNITS\n" + str(sim_units)[1:-1] + "\n"
            header_str += header_number_images
            header_str += str(sim_vars)[1:-1] + "\n"
            footer = "# UNITS_BEGIN_END\n" + str(sim_units_end)[1:-1] + "\n"
            footer += str(sim_vars_end)[1:-1] + "\n"
            str_values = ""
            for var in sim_vars_end:
                str_values += str(aq.get(var)) + ","
            footer += str_values[:-1] + "\n"

            f.write(header_str)
            f_i.write(header_number_images)
            allvars = []

            for var in sim_vars[:-1]:
                aq_var = aq.find(var)
                aq_var.time = int(100 * self.pause)
                allvars.append(aq_var)

            # initialize loop
            count = 0
            start_time = time.time()

            while count < self.number_images:
                # retrieve simvars from sim
                str_values = ""
                # delta time between values retrival
                delta = time.time()
                for var_obj in allvars:
                    str_values += str(var_obj.value) + ","
                str_values += str(time.time() - start_time) + "\n"
                f.write(str_values)
                # capture and image saving
                out = self.d.screenshot()
                out = cv2.cvtColor(out, cv2.COLOR_RGB2BGR)
                image_name = self.folder_name + "/%03d.%s" % (count, self.image_format)
                f_i.write(image_name + "\n")
                cv2.imwrite(self.root+'/'+image_name, out)
                count += 1
                delta = time.time() - delta
                print("delta = %f, pause = %f" % (delta, self.pause))
                time.sleep(max(self.pause - delta, 0))
                self.progress.emit(int(100*((count+1)/self.number_images)))

            str_values = ""
            for var in sim_vars_end:
                str_values += str(aq.get(var)) + ","
            footer += str_values[:-1]
            f.write(footer)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        finally:
            f.close()
            f_i.close()
            self.finished.emit()


def frame_buffer_to_disk(d: d3dshot.D3DShot, directory=None):
    directory = d._validate_directory(directory)

    # tuple cast to ensure an immutable frame buffer
    for i, frame in enumerate(tuple(d.frame_buffer)):
        frame_pil = d.capture_output.to_pil(frame)
        frame_pil.save(f"{directory}/{len(d.frame_buffer)-i-1}.png")


class Image_recorder(Recorder):
    """
    Simplier class that only records Images (tested on 4K >= images)
    """

    def run(self):
        # initialize d3d capture
        d = d3dshot.create(capture_output="numpy")
        f_i = open(self.folder_name + "/images.txt", "w")
        # d.screenshot_to_disk_every(self.pause,self.folder_name)
        d.capture(int(self.fps))
        time.sleep(self.pause * self.number_images)
        d.stop()
        nb_frames = len(d.frame_buffer)
        frame_buffer_to_disk(d, self.folder_name)
        header_number_images = "# NUMBER OF IMAGES\n" + str(nb_frames) + "\n"
        f_i.write(header_number_images)
        try:
            [f_i.write(self.folder_name + f"/{i}.png\n") for i in range(nb_frames)]
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        finally:
            f_i.close()

