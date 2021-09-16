import numpy as np
import os
# import matplotlib.pyplot as plt
import sys
from ..utils.features import *

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