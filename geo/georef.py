from PySide2.QtCore import QObject, SIGNAL, Signal, Slot   
from utils.homography import Homography
import shutil
from osgeo import gdal, osr
import numpy as np
import os
# import matplotlib.pyplot as plt
import cv2 as cv
import sys
import time
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from utils.features import *
if not os.name == 'nt':
    # Only unusable on Windows OS (unless GDAL<3 and python = 3.5.*)
    import otbApplication
homography = Homography()

############# HELPERS #############


def coords_distance(lat1, lon1, lat2, lon2):
    'Computes the distance between 2 points in meters'
    d = np.arccos(np.sin(lat1)*np.sin(lat2)+np.cos(lat1)
                  * np.cos(lat2)*np.cos(lon1-lon2))
    return d*6371*1e3


def cal_lat_lon(lat1, lon1, d, tc):
    'Computes the coordinates from a point with its distance and heading'
    # d must be below pi/2 (a quarter of earth)
    lat = np.arcsin(np.sin(lat1)*np.cos(d)+np.cos(lat1)*np.sin(d)*np.cos(tc))
    if (np.cos(lat) == 0):
        lon = lon1
    else:
        lon = np.mod(lon1 - np.arcsin(np.sin(tc)*np.sin(d) /
                                      np.cos(lat))+np.pi, 2*np.pi) - np.pi
    return lat, lon


def angle_from_coord(p, angle):
    'Computes the angle between the true north and a point'
    p = p / np.linalg.norm(p)
    return (np.arccos(p[0]) * np.arcsin(p[1]) / abs(np.arcsin(p[1])))-angle


def load_gcps(file_input):
    'Load GCPS from a file'
    header = "mapX,mapY,pixelX,pixelY,enable,dX,dY,residual".split(',')
    gcps = np.loadtxt(file_input, skiprows=2, delimiter=',')
    gcps_d = dict(zip(header, gcps.T))
    gcps_d['pixelY'] = gcps_d['pixelY']+2400
    gcps_d['pixelX'] = gcps_d['pixelX']
    return gcps_d
############# HELPERS #############

############# STEREO GCP / RPC GEN / ORTHO REC / GEOREF #############


class StereoGCP():
    'Estimates GCP position'

    def __init__(self, center=[0, 0], pixsize=[0.5, 0.5]):
        self.center = center
        self.pixsize = pixsize

    def setPoints(self, coordinates):
        self.pt1, self.pt2 = coordinates

    def setCenter(self, center):
        self.center = center

    def setPointsList(self, points_list):
        self.points_list = points_list

    def setPixSize(self, pixsize):
        self.pixsize = pixsize

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
        pc = (points - self.center)*self.pixsize  # centered points
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
            os.remove(input)
        return exitcode


class Georeferencer(QObject):
    progress = Signal(int)
    finished = Signal()
    def __init__(self, gcp_gen, rpc_gen, rectification, dataset=None):
        super(Georeferencer, self).__init__()
        self.gcp_gen = gcp_gen
        self.rpc_gen = rpc_gen
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

    # INIT
    # INIT
    ##############################
    # SIFTS
    # SIFTS

        print("START SIFTS :")
        start_time = time.time()

        kp1, kp2, good = compute_sift(img1, img2, d=0.1)
        print(f"\t Number of features :{len(good)}")
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
        # revoir ordre car mélangé !!
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 2)
        # for otb
        np.savetxt('src_pts.txt', src_pts)
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
            img1_geo, img2_geo, d=0.3)

        cv.imwrite(img1_final, img1_geo)
        cv.imwrite(img2_final, img2_geo)
        # voir si utile ou non
        os.remove(img1_geopath)
        os.remove(img2_geopath)
        print("Temps de calcul des homolast --- %s seconds ---" %
              (time.time() - start_time))

    # HOMOGRAPHY
    # HOMOGRAPHY

        self.count += 1

############# IMAGE GENERATION #############


def generate_input_tif(gcps, image_input, image_output, elev_file="", geoid=False):
    """
    Generates a GEOTIFF with georeferencement and rpc coeficients from an images and a list of points

    Attributes
    ----------
    gcps : list
        list of computed GCPS
    image_input : str
        image input path
    image_output : str
        image output path
    elev_file : str
        The elevation file, for now only dted and tiff format worked
    geoid : bool
        Enable or not the geoid flag. MUST be use with appropriate elev_file
    Return
    ----------


    """
    # temporary files /!\ better if each instance gets a generated name
    tmp_gcps = "tmp/tmp_gcps.txt"
    tmp_geom = "tmp/tmp_geom.geom"
    # Compute GCPS and save them for OTB format
    gcps_out, gcps_gdal = convert_save_gcps(gcps, tmp_gcps)
    # Compute RPCs no geoid no dem
    generate_rpc(tmp_gcps, tmp_geom, elev_file, geoid)
    # reading rpcs
    rpc, rpc_geom = readgeom(tmp_geom)
    os.remove(tmp_geom)
    os.remove(tmp_gcps)
    # Create a copy of the original file and save it as the output filename:
    shutil.copy(image_input, image_output)
    # Open the output file for writing :
    ds = gdal.Open(image_output, gdal.GA_Update)
    # Set spatial reference:
    sr = osr.SpatialReference()
    # 2193 refers to the NZTM2000, but can use any desired projection
    sr.ImportFromEPSG(4326)

    # Apply the GCPs to the open output file:
    ds.SetGCPs(gcps_gdal, sr.ExportToWkt())
    # No RPC (not working properly)
    ds.SetMetadata(rpc, 'RPC')

    # Close the output file in order to be able to work with it in other programs:
    ds = None
    os.remove(image_input)


def convert_save_gcps(gcps, file_output):
    nb_points = gcps.shape[0]
    new_gcps = gcps.copy()
    new_gcps[:, -1] = 2400-new_gcps[:, -1]
    # 0:mapX 1:mapY 2:pixelX 3:pixelY
    gcps_gdal = [gdal.GCP(new_gcps[i][0], new_gcps[i][1], 0,
                          new_gcps[i][2], new_gcps[i][3]) for i in range(nb_points)]
    header = ['pixelX', 'pixelY', 'mapX', 'mapY']
    header_save = ','.join(header)
    np.savetxt(file_output, new_gcps[:, [
               2, 3, 0, 1]], header=header_save, fmt='%f')
    return new_gcps, gcps_gdal


def readgeom(file_input):
    'Reads and parses rpcs from a geom file (OTB)'
    f = open(file_input)
    values = f.readlines()
    f.close()
    rpc_geom = dict(map(lambda x: x.replace(
        "\n", "").replace(" ", "").split(':'), values))
    line_den_coeff_geom = [rpc_geom['line_den_coeff_%i' % i]for i in range(20)]
    line_num_coeff_geom = [rpc_geom['line_num_coeff_%i' % i]for i in range(20)]
    samp_den_coeff_geom = [rpc_geom['samp_den_coeff_%i' % i]for i in range(20)]
    samp_num_coeff_geom = [rpc_geom['samp_num_coeff_%i' % i]for i in range(20)]
    rpc = [
        "HEIGHT_OFF="+(rpc_geom['height_off']),
        "HEIGHT_SCALE="+(rpc_geom['height_scale']),
        "LAT_OFF="+(rpc_geom['lat_off']),
        "LAT_SCALE="+(rpc_geom['lat_scale']),
        "LINE_DEN_COEFF="+(' '.join(line_den_coeff_geom)),
        "LINE_NUM_COEFF="+(' '.join(line_num_coeff_geom)),
        "LINE_OFF="+(rpc_geom['line_off']),
        "LINE_SCALE="+(rpc_geom['line_scale']),
        "LONG_OFF="+(rpc_geom['long_off']),
        "LONG_SCALE="+(rpc_geom['long_scale']),
        "SAMP_DEN_COEFF="+(' '.join(samp_den_coeff_geom)),
        "SAMP_NUM_COEFF="+(' '.join(samp_num_coeff_geom)),
        "SAMP_OFF="+(rpc_geom['samp_off']),
        "SAMP_SCALE="+(rpc_geom['samp_scale'])
    ]
    return rpc, rpc_geom


if not os.name == 'nt':
    def generate_rpc(input_points, file_output, elev_file="", geoid=False):
        'Generate RPCS from a list of points and a elevation file'
        app = otbApplication.Registry.CreateApplication(
            "GenerateRPCSensorModel")
        app.SetParameterString("outgeom", file_output)
        app.SetParameterString("outstat", "outputs/stats.geom")
        app.SetParameterString("inpoints", input_points)
        app.SetParameterString("map", "epsg")
        app.SetParameterInt("map.epsg.code", 4326)
        if len(elev_file) > 0:
            if geoid:
                print("USING GEOID")
                app.SetParameterString("elev.geoid", elev_file)
            else:
                print("USING DEM")
                app.SetParameterString("elev.dem", elev_file)
        else:
            print("NO ELEVATION SPECIFIED !")

        app.ExecuteAndWriteOutput()

    def projection_gdalcmd(in_image, out_image, dem):
        """
        Warps the input image with rpcs/gcps/elevation file
        TODO : finish it

        Attributes
        ----------
        in_image : str
            image input path
        out_image : str
            image output path
        dem : str
            The elevation file, for now only dted and tiff format worked

        Return
        ----------


        """
        cmd = 'gdalwarp -rpc -to RPC_DEM={rpcPath} -of GTiff {srcPath} {outPath} -overwrite -s_srs EPSG:4326 -t_srs EPSG:3857'\
            .format(srcPath=in_image,
                    outPath=out_image,
                    rpcPath=dem)
        print(f"COMMAND:\n{cmd}")
        return os.system(cmd)
else:
    def generate_rpc(
            input_points,
            file_output,
            elev_file="",
            geoid=False):
        """
        Generate RPCS from a list of GCPS and a elevation file

        Attributes
        ----------
        gcps : list
            list of computed GCPS
        input_points : str
            points input path
        file_output : str
            geom output path, it's the file that contains the rpcs
        elev_file : str
            The elevation file, for now only dted and tiff format worked
        geoid : bool
            Enable or not the geoid flag. MUST be use with appropriate elev_file
        Return
        ----------


        """
        cmd = 'otbcli_GenerateRPCSensorModel -outgeom {file_output} -outstat {outstat} -inpoints {inpoints} "-map.epsg.code" 4326 -map "epsg" '\
            .format(
                file_output=file_output,
                outstat="stats.geom",
                inpoints=input_points,
            )
        print(cmd)
        if len(elev_file) > 0:
            if geoid:
                print("USING GEOID")
                cmd += "-elev.geoid "+str(elev_file)
            else:
                print("USING DEM")
                cmd += "-elev.dem "+str(elev_file)
        else:
            print("NO ELEVATION SPECIFIED !")
        print(f"COMMAND:\n{cmd}")
        return os.system(cmd)

    def projection_gdalcmd(
            in_image,
            out_image,
            dem):
        """
        Warps the input image with rpcs/gcps/elevation file and outputs an orthorectified/georeferenced image file

        Attributes
        ----------
        in_image : str
            image input path
        out_image : str
            image output path
        dem : str
            The elevation file, for now only dted and tiff format worked

        ----------


        """
        # replace E:/OTB-7.3.0-Win64/bin/gdalwarp.exe with your otb's gdalwarp path
        cmd = 'E:/OTB-7.3.0-Win64/bin/gdalwarp.exe -rpc -to RPC_DEM={rpcPath} -of GTiff {srcPath} {outPath} -overwrite -s_srs EPSG:4326 -t_srs EPSG:3857'\
            .format(srcPath=in_image,
                    outPath=out_image,
                    rpcPath=dem)
        print(f"COMMAND:\n{cmd}")
        return os.system(cmd)
############# IMAGE GENERATION #############
