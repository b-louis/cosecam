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
            raise Exception("Config is invalid ! Descriptor is not defined")
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
        kp1,kp2,matches = grid_matcher_brute(sdes1s, sdes2s, skp1s ,skp2s,offset)
    else:
        raise Exception("Config is invalid ! Matcher is not defined")
    return kp1, kp2, good


def list2grid(kpoints, descriptors, grid_shape, shape, offset=[0,0]):
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
        y = y-offset[1]
        x = x-offset[0]
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

def grid_matcher_brute(sdes1s, sdes2s, skp1s ,skp2s,offset=[0,0]):
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
                # match = bf.match(
                #     np.array(sdes1s[i][j]), np.array(sdes2s[i][j]))
                # match=myBruteMatch(np.array(sdes1s[i][j]), np.array(sdes2s[i][j]))
                match=myBruteMatchEuclD(
                    np.array(sdes1s[i][j]), 
                    np.array(sdes2s[i][j]),
                    np.array(skp1s[i][j]), 
                    np.array(skp2s[i][j]),
                    offset
                    )
                # Sort them in the order of their distance.
                if(len(match)>0):    
                    match = sorted(match, key=lambda x: x.distance)
                    matches[i][j] = match[0] ## TODO: Change it or add some parameters
                    src_pts.append(skp1s[i][j][match[0].queryIdx].pt)
                    dst_pts.append(skp2s[i][j][match[0].trainIdx].pt)
    return src_pts,dst_pts,matches
    
def grid_matcher_brute_(sdes1s, sdes2s, skp1s ,skp2s,offset):
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
    i=0
    j=0
    match=myBruteMatchEuclD(
        np.array(sdes1s[i][j]), 
        np.array(sdes2s[i][j]),
        np.array(skp1s[i][j]), 
        np.array(skp2s[i][j]),
        offset
        )
    # Sort them in the order of their distance.
    match = sorted(match, key=lambda x: x.distance)
    matches[i][j] = match[0] ## TODO: Change it or add some parameters
    src_pts.append(skp1s[i][j][match[0].queryIdx].pt)
    dst_pts.append(skp2s[i][j][match[0].trainIdx].pt)
    return src_pts,dst_pts,matches

def myBruteMatch(des1,des2):#,kp1s,kp2s):
    dmatchs = []
    # matchs = np.ones((len(des1),len(des2))) * np.Infinity
    matchs = np.ones((len(des1)))
    for i in range(len(des1)):
        matchs[i] = np.linalg.norm(des1[i]-des2,axis=1).argmin()
   
    # cross check
    for i in range(len(des2)):
        vals = np.linalg.norm(des2[i]-des1,axis=1)
        curr = vals.argmin()
        if matchs[curr] == i:
            dmatchs.append(cv.DMatch(curr,i,vals[curr]))
    return dmatchs
def myBruteMatchEuclD(des1,des2,kp1s,kp2s, offset=[0,0]):
    dmatchs = []
    # matchs = np.ones((len(des1),len(des2))) * np.Infinity
    ### NORMALISATION pour sift !!
    norm_sift = 4096
    norm_euc = np.sqrt(2*100*100)
    matchs = np.ones((len(des1)))
    pos1 = np.array([kp.pt for kp in kp1s])
    pos2 = np.array([kp.pt for kp in kp2s])-offset[::-1]
    for i in range(len(des1)):
        desc_distance = np.linalg.norm(des1[i]-des2,axis=1)/norm_sift
        euc_distance = np.linalg.norm(pos1[i]-pos2,axis=1)
        d = desc_distance*0.0 + euc_distance*0.95
        matchs[i] = np.linalg.norm(des1[i]-des2,axis=1).argmin()
    # cross check
    for i in range(len(des2)):
        desc_distance = np.linalg.norm(des2[i]-des1,axis=1)/norm_sift
        euc_distance = np.linalg.norm(pos2[i]-pos1,axis=1)/norm_euc
        vals = desc_distance*0.0 + euc_distance*0.95
        curr = vals.argmin()
        if matchs[curr] == i:
            dmatchs.append(cv.DMatch(curr,i,vals[curr]))
            # dmatchs.append(f"{curr} => {i}")
    # print(len(dmatchs))
    return dmatchs   