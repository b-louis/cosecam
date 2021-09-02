import numpy as np
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