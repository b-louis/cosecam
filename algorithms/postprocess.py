# from ..utils.morph import strel
import numpy as np
# from skimage import img_as_ubyte, img_as_float
# from skimage import io as skio
# import skimage.morphology as morpho
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

# ignore skimage.morph bug
# class MorphoReconstructionSegment():
#     def __init__(self, t=30, bins=32):
#         self.t = t
#         self.bins = bins

#     def process(self, input):
#         img_skit = img_as_float(input)
#         t = self.t
#         se = strel('line', t, 0)
#         mo = morpho.opening(img_skit, se)
#         bins = np.linspace(0, 180, 10)
#         mask = np.copy(img_skit)
#         for i in bins[1:]:
#             se = strel('line', t, i)
#             morp = morpho.opening(img_skit, se)
#             mo = np.maximum(morp, mo)
#         mm = (mo/np.max(mo))*255
        
#         cho=img_skit-mm
#         cho2 = np.clip(cho,0,mm.max())
#         chocho = (cho2/np.max(cho2))*255
#         return chocho.astype(np.uint8)
#         mask = np.copy(img_skit)
#         seed = np.copy((mo < img_skit)*mo)
#         rec = strel('disk', 1)
#         reco = morpho.reconstruction(seed, mask)
#         skio.imsave("reco1.jpg", reco)
#         skio.imsave("recon.jpg", img_skit-reco)
#         return img_as_ubyte(img_skit-reco)
