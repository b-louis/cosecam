import numpy as np
import cv2 as cv
import imutils


class NoProcess:
    def process(self, frames,*args):
        return frames
    def __call__(self,frames,*args):
        return frames  


class WeightMean:
    """
    
    """

    def __init__(self, a=0, b=0.7, c=0.3):
        self.a = a
        self.b = b
        self.c = c

    def computeWeightMean(self, frames):
        # we do > background = frame*A + frame1*B + frame2*C
        temp1 = cv.addWeighted(frames[1], self.b * 2, frames[2], self.c * 2, 0.0)
        return cv.addWeighted(frames[0], self.a, temp1, 1, 0.0)

    def process(self, frames):
        background = self.computeWeightMean(frames)
        return cv.absdiff(frames[0], background)


class FrameDiff:
    def process(self, frames):
        return cv.absdiff(frames[0], frames[1])


class OpticalFlow:
    def computeOpticalFlow(self, frames):
        # frame = imutils.resize(frames[0], 1500)
        # frame1 = imutils.resize(frames[1], 1500)
        frame = cv.cvtColor(frames[0], cv.COLOR_BGR2GRAY)
        frame1 = cv.cvtColor(frames[1], cv.COLOR_BGR2GRAY)
        hsv_shape = frame.shape
        if len(hsv_shape) != 3:
            hsv_shape = (hsv_shape[0], hsv_shape[1], 3)
        hsv = np.zeros(hsv_shape, dtype=np.uint8)
        hsv[..., 1] = 255
        flow = cv.calcOpticalFlowFarneback(
            frame1, frame, None, 0.5, 3, 15, 3, 5, 1.2, 0
        )
        mag, ang = cv.cartToPolar(flow[..., 0], flow[..., 1])
        hsv[..., 0] = ang * 180 / np.pi / 2
        hsv[..., 2] = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX)
        rgb = cv.cvtColor(hsv, cv.COLOR_HSV2RGB)
        gray = cv.cvtColor(rgb, cv.COLOR_RGB2GRAY)
        cv.imshow("FLOW", hsv)
        return gray

    def process(self, frames):
        return self.computeOpticalFlow(frames)


class MeanBG:
    '''
    Mean Background, temporal mean with a a low and high thresholding
    low = bg and high = bg ==> bg
    low = fg and high = bg ==> bg
    low = fg and high = fg ==> fb
    '''
    def __init__(self, alpha: float, low_threshold: int, high_threshold: int):
        self.alpha = alpha
        self.low_threshold = low_threshold
        self.high_threshold = high_threshold
        self.low_map = 0
        self.high_map = 0

    def initialize(self, data: np.ndarray):
        self.mean = np.zeros_like(data)
        self.bg = np.zeros_like(data)

    def update(self, data: np.ndarray, update_mask: np.ndarray):
        m_mean = self.mean
        alpha = self.alpha
        mean = alpha * m_mean + (1.0 - alpha) * data
        bg = (mean + 0.5).astype(np.uint8)
        if update_mask.any() :
            self.mean[update_mask] = mean[update_mask]
            self.bg[update_mask] = bg[update_mask]
        else:
            self.mean = mean
            self.bg = bg

    def subtract(self, data: np.ndarray):
        dists = np.sum((data-self.mean) ** 2, 2)
        # background=0, foreground=1
        self.low_map = dists > self.low_threshold
        self.high_map = dists > self.high_threshold


class DPMean:
    '''
    Application of MeanBG with x frames (up to user)
    '''
    def __init__(
        self,
        alpha: float = 1e-6,
        low_threshold: int = 2700,
        high_threshold: int = 2700 * 2,
    ):
        self.meanbg = MeanBG(alpha, low_threshold, high_threshold)

    def process(self, frames):
        self.meanbg.initialize(frames[0])
        for frame in frames:
            self.meanbg.subtract(frame)
            low_map = self.meanbg.low_map
            low_map[:] = 0
            self.meanbg.update(frame, low_map)
        high_map = (self.meanbg.high_map*255).astype(np.uint8)
        low_map = (self.meanbg.low_map*255).astype(np.uint8)

        return high_map,low_map,self.meanbg.bg
