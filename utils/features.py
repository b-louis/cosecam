import numpy as np
import cv2 as cv

DESCRIPTOR_SIFT = 0
DESCRIPTOR_ORB = 1
DESCRIPTOR_AKAZE = 2
MATCHER_BRUTE = 0
MATCHER_FLANN = 1
FLANN_INDEX_KDTREE = 1
FLANN_INDEX_LSH = 6

def compute_features(img1,img2,d,mode=[DESCRIPTOR_SIFT,MATCHER_FLANN]):
    descriptor = None
    index_params = None
    search_params = None
    distance_norm = None
    if(mode[0] == DESCRIPTOR_SIFT):
        descriptor = cv.SIFT_create()
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks = 50)
        distance_norm = cv.NORM_L2
    else :
        index_params= dict(algorithm = FLANN_INDEX_LSH,
                        table_number = 6, # 12
                        key_size = 12,     # 20
                        multi_probe_level = 1) #2
        search_params = dict(check=50) 
        distance_norm = cv.NORM_HAMMING
        if(mode[0] == DESCRIPTOR_ORB):
            descriptor = cv.ORB_create()
        elif(mode[0] == DESCRIPTOR_AKAZE):
            descriptor = cv.AKAZE()
        else :
            print("Config is invalid ! May not work properly ! Descriptor is not defined")
            return
    kp1, des1 = descriptor.detectAndCompute(img1,None)
    kp2, des2 = descriptor.detectAndCompute(img2,None)
    good = []
    i=0
    if(mode[0] == MATCHER_BRUTE):
        matcher = cv.BFMatcher(distance_norm, crossCheck=True)
        matches = matcher.match(des1,des2)
        matches = sorted(matches, key = lambda x:x.distance)
        for m in matches:
            if m.distance < d :
                good.append(m)
            i+=1
        
    elif(mode[0] == MATCHER_FLANN):
        matcher = cv.FlannBasedMatcher(index_params, search_params)
        matches = matcher.knnMatch(des1,des2,k=2)
        for m,n in matches:
            if m.distance < d*n.distance:
                good.append(m)
            i+=1
    else :
        print("Config is invalid ! May not work properly ! matcher is not defined")
        return 
    return kp1,kp2,good
    

def compute_sift(img1,img2,d):
    """
    computes SIFT features with a FLANN matcher  

    """
    # On initialise le descripteur SIFT
    sift = cv.SIFT_create()
    # On recupère les points du descripteur
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)
    flann = cv.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1,des2,k=2)
    # On ne garde que les points qui satisfont Lowe's ratio test.
    good = []
    i=0
    for m,n in matches:
        if m.distance < d*n.distance:
            good.append(m)
        i+=1
        # if len(good)>1000:
        #     break
    return kp1,kp2,good
def compute_orb(img1,img2,d):
    """
    computes ORB features with a BruteForce matcher  

    """
    # On initialise le descripteur SIFT
    orb = cv.ORB_create()
    # On recupère les points du descripteur
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)
    # create BFMatcher object
    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
    # Match descriptors.
    matches = bf.match(des1,des2)
    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)
    # On ne garde que les points qui satisfont Lowe's ratio test.
    good = []
    i=0
    for m in matches:
        if m.distance < d+0.5 :
            good.append(m)
        i+=1
        # if len(good)>1000:
        #     break
    return kp1,kp2,good

def compute_akaze(img1,img2,d):
    """
    computes AKAZE features with a BruteForce matcher  
    """
    # On initialise le descripteur SIFT
    akaze = cv.AKAZE_create()
    # On recupère les points du descripteur
    kp1, des1 = akaze.detectAndCompute(img1,None)
    kp2, des2 = akaze.detectAndCompute(img2,None)
    # create BFMatcher object
    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
    # Match descriptors.
    matches = bf.match(des1,des2)
    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)
    # On ne garde que les points qui satisfont Lowe's ratio test.
    good = []
    i=0
    for m in matches:
        if m.distance < d+0.5 :
            good.append(m)
        i+=1
        # if len(good)>1000:
        #     break
    return kp1,kp2,good

def compute_akaze_flann(img1,img2,threshold):
    """
    computes SIFT features with a FLANN matcher     

    """
    # On initialise le descripteur SIFT
    akaze = cv.AKAZE_create(threshold=threshold,descriptor_type=cv.AKAZE_DESCRIPTOR_MLDB_UPRIGHT)
    # On recupère les points du descripteur
    kp1, des1 = akaze.detectAndCompute(img1,None)
    kp2, des2 = akaze.detectAndCompute(img2,None)
    FLANN_INDEX_LSH = 6
    # FLANN_INDEX_KDTREE = 1
    index_paramsk= dict(algorithm = FLANN_INDEX_LSH,
                    table_number = 6, # 12
                    key_size = 12,     # 20
                    multi_probe_level = 1) #2
    # index_paramsk = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_paramsk = dict(check=50) 
    flann = cv.FlannBasedMatcher(index_paramsk,search_paramsk)
    # matchesaf = flann.knnMatch(des1.astype(np.float32),des2.astype(np.float32),k=2)
    matchesaf = flann.knnMatch(des1,des2,k=2)
    good = []
    for m,n in matchesaf:
        # if m.distance < 0.7*n.distance:
        if m.distance < 0.6*n.distance and m.distance > 0.2*n.distance:
            good.append(m)
    return kp1,kp2,good