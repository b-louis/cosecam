import cv2 as cv
import numpy as np
from imutils import resize
import skimage.measure
from enum import *
class Filters(IntEnum):
	GAUSS = 0
	MEDIAN = 1
# Not implemented yet, to replace MedianFilter and GaussFilter
class Filter():
    def __init__(self,mode=Filters.GAUSS,filter_size=1):
        filter = None
        self.mode = mode
        if(mode == Filters.GAUSS):
            filter = cv.GaussianBlur
        elif(mode == Filters.MEDIAN):
            filter = cv.medianBlur
        else:
            raise Exception("Configuration is invalid ! mode is not defined properly")

        self.filter_size = filter_size
    def process(self,input):
        mode = self.mode
        if(mode == Filters.GAUSS):
            return filter(input,(self.filter_size,self.filter_size))

        elif(mode == Filters.MEDIAN):
            return filter(input,self.filter_size)
        else:
            raise Exception("Configuration is invalid ! mode is not defined properly")
# Not implemented yet, to replace MedianFilter and GaussFilter

class MedianFilter():
    def __init__(self,filter_size=1):
        self.filter_size = filter_size
    def __call__(self,input):
        return cv.medianBlur(input,self.filter_size)
class GaussFilter():
    def __init__(self,filter_size=1):
        self.filter_size = filter_size
    def __call__(self,input):
        return cv.GaussianBlur(input,(self.filter_size,self.filter_size),0)

def medianFilter(input,filter_size=1):
    return cv.medianBlur(input,filter_size)


def tree_filter(frame,detect):
    ' Tree filtering on colors '
    # un simple and pour essayer
    kernel = np.ones((3,3),np.uint8)
    detect_resize = skimage.measure.block_reduce(detect, (4,4), np.max)
    detect_thresh = cv.threshold(detect_resize,200,255,cv.THRESH_TOZERO_INV)[1]
    detect_thresh = cv.GaussianBlur(detect_thresh,(3,3),0)
    detect_thresh = cv.threshold(detect_thresh,detect_thresh.mean(),255,cv.THRESH_BINARY)[1]
    # detect_thresh = cv.erode(detect_thresh,kernel)
    detect_thresh = cv.morphologyEx(detect_thresh,cv.MORPH_CLOSE,kernel)
    detect_resize = resize(detect_thresh,860*4,inter=cv.INTER_NEAREST)
    # HSV
    frame_hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lower_range = np.multiply([70,20,20],[179/359,255/100,255/100])  # Set the Lower range value of color in BGR
    upper_range = np.multiply([200,100,90],[179/359,255/100,255/100])   # Set the Upper range value of color in BGR
    mask = cv.inRange(frame_hsv,lower_range,upper_range) # Create a mask with range
    mask = cv.morphologyEx(mask,cv.MORPH_CLOSE,kernel)
    return cv.bitwise_and(detect_resize,mask)