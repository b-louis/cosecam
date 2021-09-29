from PySide2.QtCore import QObject, Signal
import imutils   
import numpy as np
import os
# import matplotlib.pyplot as plt
import cv2 as cv
import time
from ..utils.features import *
from ..utils.homography import Homography
from .helpers import *
from .imagegen import *

KTSTOMS = 1/1.94384

homography = Homography()
############# STEREO GCP / RPC GEN / ORTHO REC / GEOREF #############

class StereoGCP():
    'Estimates GCP position'

    def __init__(self, center=[0, 0], pix_scale=[0.5, 0.5]):
        self.center = center
        self.pix_scale = pix_scale

    def setPoints(self, coordinates):
        self.pt1, self.pt2 = coordinates

    def setCenter(self, center):
        self.center = center

    def setPointsList(self, points_list):
        self.points_list = points_list

    def setpix_scale(self, pix_scale):
        self.pix_scale = pix_scale

    def _compute_pts(self, points, D):
        """
        ***

        Attributes
        ----------
        points : list[ [[int,int],[int,int]]* ]
            List of points, img1 to img2.

        D : float
            Distance between the two centers  

        Return
        ----------


        """
        # computes PL and PR
        pc = (points - self.center)*self.pix_scale  # centered points
        p1 = pc[0]
        p2 = pc[1]
        denom = np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        return p1*D/denom

    def compute_gcp(self, points, angle, coordinates):
        """
        computes GCP for a pair of points

        Attributes
        ----------
        points : list[ [[int,int],[int,int]]* ]
            List of points, img1 to img2.
        angle : float
            Angle from image's north to true north, in radians
        coordinates : [[float,float],[float,float]]
            Coordinates from image 1 and 2 centers, in radians

        Return
        ----------


        """
        points = np.array(points)
        D = coords_distance(*coordinates[0], *coordinates[1])
        pts = self._compute_pts(points, D)
        d_pts = np.sqrt(pts[0]**2 + pts[1]**2)
        angle_pts = angle_from_coord(pts, angle)-np.pi/2
        pts = cal_lat_lon(*coordinates[0], d_pts*0.001/6371.0, angle_pts)
        return pts

    def __call__(self, pt1, pt2, points_list, angle):
        'Compute all gcps'
        coordinates = np.radians(np.array((pt1, pt2)))
        gcps = []
        for i in range(len(points_list)):
            gcp = self.compute_gcp(points_list[i], angle, coordinates)
            gcps.append(np.degrees(gcp))
        src_pts = points_list[:, 0]
        dst_pts = points_list[:, 1]

        gcps_1 = np.hstack((np.flip(gcps, 1), src_pts))  # from image 1
        gcps_2 = np.hstack((np.flip(gcps, 1), dst_pts))  # from image 2

        return gcps_1, gcps_2


class RpcGenerator():

    def __init__(self, dem):
        self.dem = dem
        os.makedirs("tmp", exist_ok=True)

    def __call__(self, input, input_rpc, gcps):
        generate_input_tif(gcps, input, input_rpc, self.dem)


class OrthoRectification():
    def __init__(self, proj_function, dem):
        self.dem = dem
        self.proj_function = proj_function

    def __call__(self, input, out):
        exitcode = self.proj_function(input, out, self.dem)
        if exitcode == 0:
            # pass
            os.remove(input)
        return exitcode


class Georeferencer(QObject):
    progress = Signal(int)
    finished = Signal()
    def __init__(self, 
                gcp_gen, 
                rpc_gen, 
                rectification, 
                dataset=None,
                d=0,
                mode=None):
        super(Georeferencer, self).__init__()
        self.gcp_gen = gcp_gen
        self.rpc_gen = rpc_gen
        self.mode = mode
        self.d = d
        self.rectification = rectification
        if dataset != None:
            self.setDataset(dataset)
        self.count = 1

    def setDataset(self, dataset, outpath=""):
        'Set the dataset and correct values with msfs time offset'
        self.dataset = dataset
        if outpath == "":
            outpath = self.dataset.root_folder + "georeferenced_" + self.dataset.folder_name
        self.fullpath = outpath
        os.makedirs(self.fullpath, exist_ok=True)
        # OFFSET
        latt_off = np.diff(dataset.getAll('PLANE_LATITUDE')).mean()
        lon_off = np.diff(dataset.getAll('PLANE_LONGITUDE')).mean()
        self.offset = np.array([latt_off, lon_off])*dataset.values[0]['TIME']

    def run(self):
        data1 = self.dataset[0]
        data2 = self.dataset[1]
        for i in range(2, self.dataset.number_images):
            self._georef(data1, data2)
            data1 = data2
            data2 = self.dataset[i]
            self.count = i
            self.progress.emit(int(100*(i+1)/self.dataset.number_images))
        self.finished.emit()
    def _georef(self, data1, data2):
        'Full georefencement function'

        start_time = time.time()

    ##############################
    # INIT
    # INIT

        print("START INIT :")

        img1_name = str(2*self.count-2).zfill(3)
        img2_name = str(2*self.count-1).zfill(3)

        img1_newpath = self.fullpath+"/tmp_"+img1_name+".tiff"
        img2_newpath = self.fullpath+"/tmp_"+img2_name+".tiff"

        img1_newpath_rpc = self.fullpath+"/tmp_rpc_"+img1_name+".tiff"
        img2_newpath_rpc = self.fullpath+"/tmp_rpc_"+img2_name+".tiff"

        img1_geopath = self.fullpath+"/"+img1_name+"_gref.tiff"
        img2_geopath = self.fullpath+"/"+img2_name+"_gref.tiff"

        img1_final = self.fullpath+"/"+img1_name+".jpg"
        img2_final = self.fullpath+"/"+img2_name+".jpg"

        img1, val1 = data1.values()
        img2, val2 = data2.values()

        cv.imwrite(img1_newpath, img1)
        cv.imwrite(img2_newpath, img2)

        coord1 = (val1['PLANE_LATITUDE'], val1['PLANE_LONGITUDE'])
        coord2 = (val2['PLANE_LATITUDE'], val2['PLANE_LONGITUDE'])

        self.angle = (val1['HEADING_INDICATOR']+val2['HEADING_INDICATOR'])/2
        print("Temps de calcul init --- %s seconds ---" %
              (time.time() - start_time))
        
        # due to offset during capture, it's difficult to use
        # these value to compute pixel offset between two captures

        # speed = (val1['AIRSPEED_INDICATED']+val2['AIRSPEED_INDICATED'])/2
        # deltat= val2['TIME']-val1['TIME']
        # speed_ms = speed*KTSTOMS
        # d_pixel = speed_ms*deltat/self.dataset.pix_scale

        # to bypass this problem, we do a homogrphy 

        d_pixel = homography.global_homgraphy(img1,img2,d=0.7,factor=8,only_deltas=True,mode=[Descriptors.BRISK,Matchers.FLANN])


    # INIT
    # INIT
    ##############################
    # SIFTS
    # SIFTS
        # self.mode[1]=Matchers.CUSTOM
        print("START FEATURES MATCHING WITH :")
        print(" Descriptor => "+self.mode[0].name)
        print(" Matcher => "+self.mode[1].name)
        # print(" Matcher => "+self.mode[1].name)
        start_time = time.time()
    # For resizing
        # resized = 1200
        # resized_factor = 3840/resized
        # img1r = imutils.resize(img1,resized)
        # img2r = imutils.resize(img2,resized)
        # print(f"d_pixeld_pixeld_pixel {d_pixel}")
    # For resizing
        if(self.mode[1] == Matchers.CUSTOM):
            kp1, kp2, good = compute_features(img1, img2, self.d,mode=self.mode,offset=d_pixel)
        else:
            kp1, kp2, good = compute_features(img1, img2, self.d,mode=self.mode)
        
        nb_features=len(good)
        print(f"\t Number of features :{nb_features}")
        print("Temps de calcul des descripteurs --- %s seconds ---" %
              (time.time() - start_time))

    # SIFTS
    # SIFTS
    ##############################
    # GCPS
    # GCPS

        print("START GCPS :")
        print(f"\t GCPS OFFSET :{self.offset[::-1]}")

        start_time = time.time()

        src_pts = [kp1[m.queryIdx].pt for m in good]
        dst_pts = [kp2[m.trainIdx].pt for m in good]

        # src_pts = resized_factor*np.float32(src_pts).reshape(-1, 2)
        # dst_pts = resized_factor*np.float32(dst_pts).reshape(-1, 2)
        src_pts = np.float32(src_pts).reshape(-1, 2)
        dst_pts = np.float32(dst_pts).reshape(-1, 2)
        # for otb
        np.savetxt('src_pts.txt', src_pts)
        np.savetxt('dst_pts.txt', dst_pts)
        src_pts[:, 1] = 2400-src_pts[:, 1]
        dst_pts[:, 1] = 2400-dst_pts[:, 1]
        pix_coords = np.array(list(zip(src_pts, dst_pts)))

        gcps_1, gcps_2 = self.gcp_gen(coord1, coord2, pix_coords, self.angle)

        gcps_1[:, 0:2] -= self.offset[::-1]
        gcps_2[:, 0:2] -= self.offset[::-1]
        print("Temps de calcul des Gcps --- %s seconds ---" %
              (time.time() - start_time))

    # GCPS
    # GCPS
    ##############################
    # RPCS
    # RPCS

        print("START RPCS :")
        start_time = time.time()

        self.rpc_gen(img1_newpath, img1_newpath_rpc, gcps_1)
        self.rpc_gen(img2_newpath, img2_newpath_rpc, gcps_2)
        print("Temps de calcul des Rpcs --- %s seconds ---" %
              (time.time() - start_time))

    # RPCS
    # RPCS
    ##############################
    # ORTHORECTIFICATION
    # ORTHORECTIFICATION

        print("START ORTHORECT :")

        start_time = time.time()

        self.rectification(img1_newpath_rpc, img1_geopath)
        self.rectification(img2_newpath_rpc, img2_geopath)
        print("Temps de calcul orhot --- %s seconds ---" %
              (time.time() - start_time))

    # ORTHORECTIFICATION
    # ORTHORECTIFICATION
    ##############################
    # HOMOGRAPHY
    # HOMOGRAPHY

        print("START HOMGRAPHY :")
        start_time = time.time()
        img1_geo = cv.imread(img1_geopath)
        img2_geo = cv.imread(img2_geopath)

        img1_geo, img2_geo = homography.global_homgraphy(
            img1_geo, img2_geo, d=0.7)

        cv.imwrite(img1_final, img1_geo)
        cv.imwrite(img2_final, img2_geo)
        # exit()

        os.remove(img1_geopath)
        os.remove(img2_geopath)
        print("Temps de calcul des homolast --- %s seconds ---" %
              (time.time() - start_time))

    # HOMOGRAPHY
    # HOMOGRAPHY

        self.count += 1

