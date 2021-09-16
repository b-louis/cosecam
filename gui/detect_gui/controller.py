import numpy as np
import cv2 as cv
import sys
import os
import traceback
from ...utils import *
from ...algorithms import *
from imutils import paths, resize
from PySide2.QtCore import QObject, SIGNAL, Signal, Slot   
BOUND_ADD = 10
BASE_DELTAT = 10
class DetectionWorker(QObject):
    progress = Signal(int)
    nextstep = Signal(np.ndarray)
    finished = Signal()
    def __init__(self):
        super(DetectionWorker,self).__init__()
        self.imagePath=[]
        self.stop = False
    def setStop(self):
        self.stop = True
    def setConfig(
        self,
        detection,
        preprocess,
        postprocess,
        threshold,
        threshold_postprocess):

        self.detection = detection
        self.preprocess = preprocess
        self.postprocess = postprocess
        self.threshold = threshold
        self.threshold_postprocess = threshold_postprocess
    def get_overlap_area(self,img1,img2):
        mask1 = ((img1.sum(2))>3)*1.0
        mask2 = ((img2.sum(2))>3)*1.0
        out = np.bitwise_and(mask1!=0,mask2!=0)*1.0
        out = cv.normalize(out, None, alpha = 0, beta = 255, norm_type = cv.NORM_MINMAX, dtype = cv.CV_32F)
        out = cv.erode(out,np.ones((9,9)))
        out = cv.normalize(out, None, alpha = 0, beta = 255, norm_type = cv.NORM_MINMAX, dtype = cv.CV_8U)
        # cv.imwrite("out.bmp",out)
        nimg1 = cv.bitwise_and(img1,img1,mask = out)
        nimg2 = cv.bitwise_and(img2,img2,mask = out)
        return nimg1,nimg2
    def set_image(self,imagePath):
        self.imagePath = imagePath
    def run(self):
        imagePath = self.imagePath
        try:
            for i in range(len(imagePath)) :
                img1 = cv.imread(imagePath[i][0])
                img2 = cv.imread(imagePath[i][1])
                ##### Overlap region selection #####
                nimg1,nimg2 = self.get_overlap_area(img1,img2)
                ####################################

                nimgs = [nimg1,nimg2]
                
                nimgsp =[self.preprocess(im) for im in nimgs]
                result = nimgs[-1]
                nimgse = [cv.cvtColor(im, cv.COLOR_BGR2GRAY) for im in nimgsp]
                frames = nimgse
                detect = []
                
                if(isinstance(self.detection,detection.DPMean)):
                    detect,_,_ = self.detection.process(nimgsp)
                else:
                    detect = self.detection.process(frames)

                post = self.postprocess(detect,5)
                thresh = self.threshold.process(post)
                contours, hierachy = cv.findContours(
                    thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
                contours_bound = [cv.boundingRect(c) for c in contours]
                contours = contours_bound
                temp_img = np.zeros_like(thresh)
                for cntr in contours:
                    x, y, w, h = cntr
                    cv.rectangle(result, (x-BOUND_ADD, y-BOUND_ADD),
                                (x+w+BOUND_ADD, y+h+BOUND_ADD), (255, 0, 0), 2)
                # Rewrite the temp file location
                os.makedirs("tmp_imgs",exist_ok=True)
                os.makedirs("tmp_imgs/thresh/",exist_ok=True)
                os.makedirs("tmp_imgs/result/",exist_ok=True)
                os.makedirs("tmp_imgs/post/",exist_ok=True)
                os.makedirs("tmp_imgs/detect/",exist_ok=True)

                cv.imwrite("tmp_imgs/thresh.png",thresh)
                cv.imwrite("tmp_imgs/result.png",result)
                cv.imwrite("tmp_imgs/post.png",post)
                cv.imwrite("tmp_imgs/detect.png",detect)
                
                cv.imwrite(f"tmp_imgs/thresh/{i}.png",thresh)
                cv.imwrite(f"tmp_imgs/result/{i}.png",result)
                cv.imwrite(f"tmp_imgs/post/{i}.png",post)
                cv.imwrite(f"tmp_imgs/detect/{i}.png",detect)

                self.nextstep.emit(detect)
                if self.stop:
                    self.stop = False
                    break
        except Exception as e:
            print(traceback.format_exc())
            raise
        self.finished.emit()
    
    def _run(self,imagePath):
        img1 = cv.imread(imagePath[0])
        img2 = cv.imread(imagePath[1])


        ##### Overlap region selection #####
        nimg1,nimg2 = self.get_overlap_area(img1,img2)
        ####################################

        nimgs = [nimg1,nimg2]
        
        nimgsp =[self.preprocess(im) for im in nimgs]
        result = nimgs[-1]
        nimgse = [cv.cvtColor(im, cv.COLOR_BGR2GRAY) for im in nimgsp]
        frames = nimgse
        if(isinstance(self.detection,detection.DPMean)):
            detect,_,_ = self.detection.process(frames)
        else:
            detect = self.detection.process(frames)

        post = self.postprocess(detect,5)
        thresh = self.threshold.process(post)
        contours, hierachy = cv.findContours(
            thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        contours_bound = [cv.boundingRect(c) for c in contours]
        contours = contours_bound
        temp_img = np.zeros_like(thresh)
        for cntr in contours:
            x, y, w, h = cntr
            cv.rectangle(result, (x-BOUND_ADD, y-BOUND_ADD),
                        (x+w+BOUND_ADD, y+h+BOUND_ADD), (255, 0, 0), 2)

        self.finished.emit()
        os.makedirs("tmp_imgs",exist_ok=True)
        cv.imwrite("tmp_imgs/thresh.png",thresh)
        cv.imwrite("tmp_imgs/result.png",result)
        cv.imwrite("tmp_imgs/post.png",post)
        cv.imwrite("tmp_imgs/detect.png",detect)
        return thresh, post ,detect
