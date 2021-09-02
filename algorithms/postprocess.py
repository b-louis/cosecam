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

def apply_brightness_contrast(input_img, brightness=0, contrast=0):

    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow)/255
        gamma_b = shadow

        buf = cv.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()

    if contrast != 0:
        f = 131*(contrast + 127)/(127*(131-contrast))
        alpha_c = f
        gamma_c = 127*(1-f)

        buf = cv.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    return buf

