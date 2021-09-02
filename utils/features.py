import numpy as np
import cv2 as cv

def compute_sift(img1,img2,d):
    """
    This function computes the formula ...
    TODO : finish it

    Attributes
    ----------
    points : list[ [[int,int],[int,int]]* ]
        List of points, img1 to img2.

    D : float
        Distance between the two centers  
    
    Return
    ----------
    

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
