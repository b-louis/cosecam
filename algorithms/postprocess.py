import numpy as np
import cv2 as cv

class MedianDilate():
    def __init__(self, kernel=np.ones((12, 12), np.uint8), blur_size=1):
        self.kernel = kernel
        self.blur_size = blur_size

    def process(self, input):
        kernel = self.kernel
        output = cv.medianBlur(input, self.blur_size)
        output = cv.dilate(output, kernel)
        return output
    def __call__(self, input,x):
        return self.process(input)

