import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import time

from .features import *

MIN_MATCH_COUNT = 10

class Homography:
    def __init__(self,d=0.7,mode=[Descriptors.SIFT,Matchers.FLANN]):
        self.mode = mode
        self.d = d
    def global_homgraphy(self,img1,img2,d):
        """
        Computes the global homography 

        Attributes
        ----------
        img1 : np.array[]
            Array representing a image

        img2 : np.array[]
            Array representing a image

        d : float
            discriminating value between keypoints  
        
        Return
        ----------
        

        """
        d=self.d
        start_timer = time.time()

        # L'homographie est faite a une echelle différent (plus basse)
        img1_size = img1.shape[:2]
        img2_size = img2.shape[:2]
        outsize = np.max([img1_size,img2_size],0)
        pad1=outsize-img1_size 
        pad2=outsize-img2_size 
        img1 = cv.copyMakeBorder(img1,0,*pad1,0,cv.BORDER_CONSTANT)
        img2 = cv.copyMakeBorder(img2,0,*pad2,0,cv.BORDER_CONSTANT)

        # la matrice d'echelle de l'homography
        S = np.array([[1,0,0],[0,1,0],[0,0,1]])
        # Cela permet d'avoir moins de descripteur et moins de pixels pour l'homographie
        # kp1,kp2,good = compute_sift(img1,img2,d)
        # kp1,kp2,good = compute_orb(img1,img2,30)
        kp1,kp2,good = compute_features(img1,img2,d,self.mode)
        print("Temps de calcul des descripteurs --- %s seconds ---" % (time.time() - start_timer))
        start_timer = time.time()
        if len(good)>MIN_MATCH_COUNT:

            if(self.mode[1] == Matchers.CUSTOM):
                src_pts = kp1
                dst_pts = kp2
            else:
                src_pts = [kp1[m.queryIdx].pt for m in good]
                dst_pts = [kp2[m.trainIdx].pt for m in good]

            H, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC,5.0)
            # M' = S . H . S-1 
            H = np.dot(np.dot(S,H),np.linalg.inv(S))
            h,w,d = img1.shape
            pts = np.float32([ [0,0],[0,h],[w,h],[w,0] ]).reshape(-1,1,2)
            
            # dst correspond aux nouveaux bords de l'image.
            dst = cv.perspectiveTransform(pts,H)
            tx = abs(round(max(np.max(dst[0]),np.min(dst[3]))))
            ty = round(max(np.min(dst[0]),np.min(dst[1])))
            # on effectue l'homgraphie
            img2_warp = cv.warpPerspective(img2, H, (img2.shape[1], img2.shape[0]),flags=(cv.WARP_INVERSE_MAP+cv.INTER_CUBIC ))
            
            # L'idée de recupérer seulement les parties de l'image qui se recollent
            print("Temps pour l'homographie --- %s seconds ---" % (time.time() - start_timer))
            return img1,img2_warp
        else:
            print("CRASH in homography")
            return

def main():
    homography = Homography()
    img1 = cv.imread('E:/Repos/depth/000.jpg')
    img2 = cv.imread('E:/Repos/depth/001.jpg')
    newi1, newi2 = homography.global_homgraphy(img1,img2,d=30)
    cv.imwrite('E:/Repos/depth/newi11.png',newi1)
    cv.imwrite('E:/Repos/depth/newi22.png',newi2)


if __name__ == '__main__':
    main()