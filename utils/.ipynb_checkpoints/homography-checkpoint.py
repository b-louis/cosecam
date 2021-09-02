import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import time
import imutils

start_time = time.time()
MIN_MATCH_COUNT = 100
RESHAPE_WIDTH = 500

class Homography:
    @classmethod
    def compute_sift(cls,img1,img2):
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
        for m,n in matches:
            if m.distance < 0.7*n.distance:
                good.append(m)
            # if len(good)>1000:
            #     break
        return kp1,kp2,des1,des2,good
    @classmethod
    def global_homgraphy(cls,img1,img2,min_match=MIN_MATCH_COUNT,reshape_width=RESHAPE_WIDTH):
        global start_time

        # L'homographie est faite a une echelle différent (plus basse)
        img1_low = img1.copy()
        img2_low = img2.copy()
        fullsize = img1.shape[0:2]
        ratio = fullsize[1]/RESHAPE_WIDTH
        # la matrice d'echelle de l'homography
        S = np.array([[ratio,0,0],[0,ratio,0],[0,0,1]])
        # Cela permet d'avoir moins de descripteur et moins de pixels pour l'homographie
        img1_low = imutils.resize(img1,width=RESHAPE_WIDTH)
        img2_low = imutils.resize(img2,width=RESHAPE_WIDTH)
        kp1,kp2,des1,des2,good = cls.compute_sift(img1_low,img2_low)
        print("Temps de calcul des descripteurs --- %s seconds ---" % (time.time() - start_time))
        start_time = time.time()
        # print(len(good))
        if len(good)>MIN_MATCH_COUNT:
            src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
            dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
            H, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC,5.0)
            # M' = S . H . S-1 
            H = np.dot(np.dot(S,H),np.linalg.inv(S))
            h,w,d = img1.shape
            pts = np.float32([ [0,0],[0,h],[w,h],[w,0] ]).reshape(-1,1,2)
            
            # dst correspond aux nouveaux bords de l'image.
            dst = cv.perspectiveTransform(pts,H)
            # ty = abs(round(max(dst[0,0,0],dst[1,0,0],key=abs)))
            # tx = abs(round(max(dst[0,0,1],dst[3,0,1],key=abs)))
            ty = 50
            tx = 50
            # print(dst)
            # on effectue l'homgraphie
            img2_warp = cv.warpPerspective(img2, H, (img2.shape[1], img2.shape[0]),flags=(cv.WARP_INVERSE_MAP+cv.INTER_CUBIC ))
            
            # L'idée de recupérer seulement les parties de l'image qui se recollent
            img1_warp = img1[tx:,ty:,:]
            img2_warp = img2_warp[tx:,ty:,:]
            print(img2_warp.shape)

            print("Temps pour l'homographie --- %s seconds ---" % (time.time() - start_time))
            return img1_warp,img2_warp
        else:
            return
        
