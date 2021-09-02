# from ..utils.morph import strel
import numpy as np
# from skimage import img_as_ubyte, img_as_float
# from skimage import io as skio
# import skimage.morphology as morpho
import cv2 as cv


class Opening():
    def __init__(self, kernel=(3, 3)):
        self.kernel = kernel

    def process(self, input):
        kernel = self.kernel
        print(kernel)
        output = cv.morphologyEx(input, cv.MORPH_OPEN,kernel)
        return output
    def __call__(self, input,x):
        return self.process(input)