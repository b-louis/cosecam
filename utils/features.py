import cv2 as cv
import numpy as np
from enum import *


class Descriptors(IntEnum):
    SIFT = 0
    ORB = 1
    AKAZE = 2
    BRISK = 3


class Matchers(IntEnum):
    FLANN = 0
    BRUTEFORCE = 1
    CUSTOM = 2


FLANN_INDEX_KDTREE = 1
FLANN_INDEX_LSH = 6


def compute_features(
    img1, 
    img2, 
    d, 
    mode=[Descriptors.SIFT, Matchers.FLANN], 
    offset=0, 
    grid_shape=100
    ):
    """
        Function that computes matched key points.

        Multiple descriptor are available:
                SIFT
            ORB
            AKAZE
            BRISK

        Multiple matcher are available:
            FLANN
            BRUTEFORCE
            CUSTOM
    """
    descriptor = None
    index_params = None
    search_params = None
    distance_norm = None
    if(mode[0] == Descriptors.SIFT):
        descriptor = cv.SIFT_create()
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)
        distance_norm = cv.NORM_L2
    else:
        index_params = dict(algorithm=FLANN_INDEX_LSH,
                            table_number=6,  # 12
                            key_size=12,     # 20
                            multi_probe_level=1)  # 2
        search_params = dict(check=50)
        distance_norm = cv.NORM_HAMMING
        if(mode[0] == Descriptors.ORB):
            descriptor = cv.ORB_create()
        elif(mode[0] == Descriptors.AKAZE):
            descriptor = cv.AKAZE_create()
        elif(mode[0] == Descriptors.BRISK):
            descriptor = cv.BRISK_create()
        else:
            print("Config is invalid ! May not work properly ! Descriptor is not defined")
            return
    kp1, des1 = descriptor.detectAndCompute(img1, None)
    kp2, des2 = descriptor.detectAndCompute(img2, None)
    good = []
    i = 0
    if(mode[1] == Matchers.BRUTEFORCE):
        matcher = cv.BFMatcher(distance_norm, crossCheck=True)
        matches = matcher.match(des1, des2)
        matches = sorted(matches, key=lambda x: x.distance)
        for m in matches:
            if m.distance < d:
                good.append(m)
            i += 1

    elif(mode[1] == Matchers.FLANN):
        matcher = cv.FlannBasedMatcher(index_params, search_params)
        matches = matcher.knnMatch(des1, des2, k=2)
        for m, n in matches:
            if m.distance < d*n.distance:
                good.append(m)
            i += 1
    elif(mode[1] == Matchers.CUSTOM):
        shape = np.ceil(np.array(img1.shape[:-1])/100).astype(int)
        skp1s, sdes1s = list2grid(kp1, des1, 100, shape)
        skp2s, sdes2s = list2grid(kp2, des2, 100, shape, offset)
        kp1,kp2,matches = grid_matcher_brute(sdes1s, sdes2s, skp1s ,skp2s)
    else:
        print("Config is invalid ! May not work properly ! matcher is not defined")
        return
    return kp1, kp2, good


def list2grid(kpoints, descriptors, grid_shape, shape, offset=0):
    """ 
    We split the image into a grid, each cell contains descriptors
    
    """
    # l,h = np.ceil(np.array(img1.shape[:-1])/grid_shape).astype(int)
    l, h = shape
    grid_kps = [[[] for j in range(h)]for i in range(l)]
    grid_des = [[[] for j in range(h)]for i in range(l)]

    for i in range(len(kpoints)):
        kp = kpoints[i]
        y, x = kp.pt
        x = x-offset
        i_grid = int(x//grid_shape)
        j_grid = int(y//grid_shape)
        if(
            i_grid >= l or i_grid < 0 or
            j_grid >= h or j_grid < 0
        ):
            continue
        grid_kps[i_grid][j_grid].append(kp)
        grid_des[i_grid][j_grid].append(descriptors[i])

    return grid_kps, np.array(grid_des)

def grid_matcher_brute(sdes1s, sdes2s, skp1s ,skp2s):
    """ 
    We compute the matcher on each cells, this is done locally to gain more time
    
    """
    # l,h = np.ceil(np.array(img1.shape[:-1])/100).astype(int)
    l, h = sdes1s.shape
    bf = cv.BFMatcher(cv.NORM_L2, crossCheck=True)
    # Match descriptors.
    matches = [[[] for j in range(h)]for i in range(l)]
    src_pts = []
    dst_pts = []
    for i in range(l):
        for j in range(h):
            if len(sdes1s[i][j]) != 0 and len(sdes2s[i][j]) != 0:
                match = bf.match(
                    np.array(sdes1s[i][j]), np.array(sdes2s[i][j]))
                # Sort them in the order of their distance.
                match = sorted(match, key=lambda x: x.distance)
                matches[i][j] = match[0] ## TODO: Change it or add some parameters
                src_pts.append(skp1s[i][j][match[0].queryIdx].pt)
                dst_pts.append(skp2s[i][j][match[0].trainIdx].pt)
    return src_pts,dst_pts,matches

## OLD , must be deleted ##
## OLD , must be deleted ##
## OLD , must be deleted ##
## OLD , must be deleted ##
## OLD , must be deleted ##
## OLD , must be deleted ##


def compute_sift(img1, img2, d):
    """
    computes SIFT features with a FLANN matcher  

    """
    # On initialise le descripteur SIFT
    sift = cv.SIFT_create()
    # On recupère les points du descripteur
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)
    # On ne garde que les points qui satisfont Lowe's ratio test.
    good = []
    i = 0
    for m, n in matches:
        if m.distance < d*n.distance:
            good.append(m)
        i += 1
        # if len(good)>1000:
        #     break
    return kp1, kp2, good


def compute_orb(img1, img2, d):
    """
    computes ORB features with a BruteForce matcher  

    """
    # On initialise le descripteur SIFT
    orb = cv.ORB_create()
    # On recupère les points du descripteur
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
    # create BFMatcher object
    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
    # Match descriptors.
    matches = bf.match(des1, des2)
    # Sort them in the order of their distance.
    matches = sorted(matches, key=lambda x: x.distance)
    # On ne garde que les points qui satisfont Lowe's ratio test.
    good = []
    i = 0
    for m in matches:
        if m.distance < d+0.5:
            good.append(m)
        i += 1
        # if len(good)>1000:
        #     break
    return kp1, kp2, good


def compute_akaze(img1, img2, d):
    """
    computes AKAZE features with a BruteForce matcher  
    """
    # On initialise le descripteur SIFT
    akaze = cv.AKAZE_create()
    # On recupère les points du descripteur
    kp1, des1 = akaze.detectAndCompute(img1, None)
    kp2, des2 = akaze.detectAndCompute(img2, None)
    # create BFMatcher object
    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
    # Match descriptors.
    matches = bf.match(des1, des2)
    # Sort them in the order of their distance.
    matches = sorted(matches, key=lambda x: x.distance)
    # On ne garde que les points qui satisfont Lowe's ratio test.
    good = []
    i = 0
    for m in matches:
        if m.distance < d+0.5:
            good.append(m)
        i += 1
        # if len(good)>1000:
        #     break
    return kp1, kp2, good


def compute_akaze_flann(img1, img2, threshold):
    """
    computes SIFT features with a FLANN matcher     

    """
    # On initialise le descripteur SIFT
    akaze = cv.AKAZE_create(threshold=threshold,
                            descriptor_type=cv.AKAZE_DESCRIPTOR_MLDB_UPRIGHT)
    # On recupère les points du descripteur
    kp1, des1 = akaze.detectAndCompute(img1, None)
    kp2, des2 = akaze.detectAndCompute(img2, None)
    FLANN_INDEX_LSH = 6
    # FLANN_INDEX_KDTREE = 1
    index_paramsk = dict(algorithm=FLANN_INDEX_LSH,
                         table_number=6,  # 12
                         key_size=12,     # 20
                         multi_probe_level=1)  # 2
    # index_paramsk = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_paramsk = dict(check=50)
    flann = cv.FlannBasedMatcher(index_paramsk, search_paramsk)
    # matchesaf = flann.knnMatch(des1.astype(np.float32),des2.astype(np.float32),k=2)
    matchesaf = flann.knnMatch(des1, des2, k=2)
    good = []
    for m, n in matchesaf:
        # if m.distance < 0.7*n.distance:
        if m.distance < 0.6*n.distance and m.distance > 0.2*n.distance:
            good.append(m)
    return kp1, kp2, good
