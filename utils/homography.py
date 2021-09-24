import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import time
import imutils

from .features import *
MIN_MATCH_COUNT = 10

class Homography:
    def global_homgraphy(self,img1,img2,d=0.7,factor=1,only_deltas=False,mode=[Descriptors.SIFT,Matchers.FLANN]):
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
        start_timer = time.time()

    #### Incase we have different image size (gdalwarp generates images with differents sizes)
        img1_size = img1.shape[:2]
        img2_size = img2.shape[:2]
        outsize = np.max([img1_size,img2_size],0)
        pad1=outsize-img1_size 
        pad2=outsize-img2_size 
        img1 = cv.copyMakeBorder(img1,0,*pad1,0,cv.BORDER_CONSTANT)
        img2 = cv.copyMakeBorder(img2,0,*pad2,0,cv.BORDER_CONSTANT)
    ####
        img1_hom = img1.copy()
        img2_hom = img2.copy()
        if factor >1 :
            reshape_width = int(img1.shape[1]/factor)
            img1_hom = imutils.resize(img1,width=reshape_width)
            img2_hom = imutils.resize(img2,width=reshape_width)
        # homography scale matrix
        S = np.array([[factor,0,0],[0,factor,0],[0,0,1]])

        # Cela permet d'avoir moins de descripteur et moins de pixels pour l'homographie
        kp1,kp2,good = compute_features(img1_hom,img2_hom,d,mode)
        print("Time for descriptor computation --- %s seconds ---" % (time.time() - start_timer))
        start_timer = time.time()
        if len(good)>MIN_MATCH_COUNT:

            if(mode[1] == Matchers.CUSTOM):
                src_pts = kp1
                dst_pts = kp2
            else:
                src_pts = [kp1[m.queryIdx].pt for m in good]
                dst_pts = [kp2[m.trainIdx].pt for m in good]

            src_pts = np.float32(src_pts).reshape(-1,1,2)
            dst_pts = np.float32(dst_pts).reshape(-1,1,2)

            H, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC,5.0)
            # M' = S . H . S-1 
            H = np.dot(np.dot(S,H),np.linalg.inv(S))
            h,w,d = img1.shape
            pts = np.float32([ [0,0],[0,h],[w,h],[w,0] ]).reshape(-1,1,2)
            
            # dst correspond aux nouveaux bords de l'image.
            dst = cv.perspectiveTransform(pts,H)
            if only_deltas:

                tx = abs(round(max(np.max(dst[0]),np.min(dst[3]))))
                ty = round(max(np.min(dst[0]),np.min(dst[1])))
            
                print(f"deltax {tx} | deltay {ty}")
                print("Time for deltas computation --- %s seconds ---" % (time.time() - start_timer))

                return tx,ty
            # on effectue l'homgraphie
            img2_warp = cv.warpPerspective(img2, H, (img2.shape[1], img2.shape[0]),flags=(cv.WARP_INVERSE_MAP+cv.INTER_CUBIC ))
            
            # L'idée de recupérer seulement les parties de l'image qui se recollent
            print("Time for homography --- %s seconds ---" % (time.time() - start_timer))
            return img1,img2_warp
        else:
            raise Exception("Not enough matched points")

def main():
    homography = Homography()
    img1 = cv.imread('H:/images_database/124_paris_1/020.png')
    img2 = cv.imread('H:/images_database/124_paris_1/021.png')
    newi1, newi2 = homography.global_homgraphy(img1,img2,d=0.7,factor=10)
    cv.imwrite('E:/Repos/depth/000r.png',newi1)
    cv.imwrite('E:/Repos/depth/001r.png',newi2)


if __name__ == '__main__':
    main()