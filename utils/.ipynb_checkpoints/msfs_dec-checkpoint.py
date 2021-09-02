import cv2
import time
import imutils
import os
import sys
import numpy as np
from ..config import *
import cv2 as cv
# TODO: 
# Less repitions in code
class Msfs_img_only_decoder:

    '''
    Reading images from txt files 
    '''

    def __init__(self, root_folder: str, folder_name: str,):
        self.root_folder = root_folder
        self.folder_name = folder_name
        self.n = 0

        f_images = root_folder + "/" + folder_name + "/images.txt"
        f_i = open(f_images)
        try:
            self.images = np.loadtxt(f_i, skiprows=2, delimiter=",", dtype=str)
            self.number_images = len(self.images)
        except Exception:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        f_i.close()

    def __getitem__(self, key: int):
        return cv.imread(self.root_folder + "/" + self.images[key])

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.number_images:
            out = self[self.n]
            self.n += 1
            return out
        else:
            raise StopIteration

    def initial_image(self):
        return self[0]

    def next_image(self):
        if self.n < self.number_images:
            self.n += 1
        return self[self.n]

    def previous_image(self):
        if 0 < self.n:
            self.n -= 1
        return self[self.n]

    @property
    def current_frame(self):
        return self.n

class Msfs_path_decoder:
    '''
    Reading path and values from txt to orthorectifiction 
    '''

    def __init__(self, root_folder: str, folder_name: str,):
        self.root_folder = root_folder
        self.folder_name = folder_name
        self.n = 0

        f_images = root_folder + "/" + folder_name + "/images.txt"
        f_i = open(f_images)
        try:
            self.images = np.loadtxt(f_i, skiprows=2, delimiter=",", dtype=str)
            self.number_images = len(self.images)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        f_i.close()

    def __getitem__(self, key: int):
        return cv.imread(self.root_folder + "/" + self.images[key])

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.number_images:
            out = self[self.n]
            self.n += 1
            return out
        else:
            raise StopIteration

    def initial_image(self):
        return self[0]

    def next_image(self):
        if self.n < self.number_images:
            self.n += 1
        return self[self.n]

    def previous_image(self):
        if 0 < self.n:
            self.n -= 1
        return self[self.n]

    @property
    def current_frame(self):
        return self.n

class Msfs_decoder:
    '''
    Reading images and values from txt files 
    '''

    def __init__(self, root_folder: str, folder_name: str, only_path: bool = False, only_images: bool = False):
        self.only_path = only_path
        self.only_images = only_images
        if only_images:
            self._only_img_init(root_folder,folder_name)
        else:
            self._full_init(root_folder,folder_name)
    def _full_init(self,root_folder, folder_name):
        def load2dict(keys,x):
            return dict(zip(keys,x))
        self.root_folder = root_folder
        self.folder_name = folder_name
        keys = config.VARS_BEGIN_END+config.VARS
        self.n = 0

        f_values = root_folder + "/" + folder_name + "/values.txt"
        f_images = root_folder + "/" + folder_name + "/images.txt"
        f = open(f_values)
        f_i = open(f_images)
        try:
            values = f.readlines()

            # first 5 lines are units,number of images and captured simvars
            self.units = values[-4].replace("'", "").strip().replace(" ", "").split(
                ","
            ) + values[1].replace("'", "").strip().replace(" ", "").split(",")
            self.number_images = int(values[3].replace("'", "").strip())
            self.simvars = values[-3].replace("'", "").strip().replace(" ", "").split(
                ","
            ) + values[4].replace("'", "").strip().replace(" ", "").split(",")
            a = values[-1].replace("'", "").strip().lstrip().split(",")
            b = values[-2].replace("'", "").strip().lstrip().split(",")
            c = np.array([a, b]).astype(np.float)

            # we reopen the file to use loadtxt
            f = open(f_values)
            values = np.loadtxt(
                f, skiprows=5, max_rows=self.number_images, delimiter=","
            )
            self.images = np.loadtxt(f_i, skiprows=2, delimiter=",", dtype=str)

            # we add the mean values of the simvars that are taken 2 times
            # at the beginning and at the end
            tiled = np.tile(c.mean(axis=0), (self.number_images, 1))
            self.values = np.concatenate((tiled, values), axis=1)

            # convert values and units to a dict for more readability
            self.values = list(map(lambda x : load2dict(keys,x),self.values))
            self.units = dict(zip(keys,self.units))

            # set image' scale (TO CHANGE !)
            self.pix_scale = 100/200 #(1/2 pixel for 1meter)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        f.close()
        f_i.close()

    def _only_img_init(self,root_folder,folder_name):
        self.root_folder = root_folder
        self.folder_name = folder_name
        self.n = 0

        f_images = root_folder + "/" + folder_name + "/images.txt"
        f_i = open(f_images)
        try:
            self.images = np.loadtxt(f_i, skiprows=2, delimiter=",", dtype=str)
            self.number_images = len(self.images)
        except Exception:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        f_i.close()

    def __getitem__(self, key: int):
        if not self.only_path:
            out = cv.imread(self.root_folder + "/" + self.images[key])
        else:
            out = self.root_folder + "/" + self.images[key]
        if self.only_images:
            return out
        return {'image':out, 'values':self.values[key]}

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.number_images:
            out = self[self.n]
            self.n += 1
            return out
        else:
            raise StopIteration

    def initial_image(self):
        return self[0]

    def next_image(self):
        if self.n < self.number_images:
            self.n += 1
        return self[self.n]

    def previous_image(self):
        if 0 < self.n:
            self.n -= 1
        return self[self.n]

    @property
    def current_frame(self):
        return self.n
