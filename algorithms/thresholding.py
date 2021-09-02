import numpy as np
import cv2 as cv
import torch
import torch.nn as nn
import kornia
from kornia.geometry import *
from kornia.morphology import *

class NoTresholding():
    def process(self,frame):
        return frame

class PourcentageThresh() :
    def __init__(self,treshold_hist=0.9,factor=1.3):
        self.treshold_hist = treshold_hist
        self.factor = factor
    def process(self,frame):

        _frame = frame[frame>25]
        hist,_ = np.histogram(_frame.ravel(),256,[0,256])
        hist_cumsum = np.cumsum(hist)/np.sum(hist)
        # on prend a partir d'un pourcentage
        thresh_hist = np.argmax(hist_cumsum>self.treshold_hist)
        print(f"thresh_hist {thresh_hist} hist {np.sum(hist)}")

    #################OLD!!#######################
        # on calcul le gradient de l'histogramme
        # grad_hist = np.gradient(hist_cumsum[thresh_hist:])

        # l'instant où la somme devient de plus en plus constante
        # hist_bump = np.argmax(grad_hist<self.factor)
        # threshold = (thresh_hist + hist_bump)*1.3

        # (on peut s'imaginer que l'on était dans une sorte de creux)
        # _, diff_thresh = cv.threshold(frame,threshold,255,cv.THRESH_BINARY)
    #################OLD!!#######################

        _, diff_thresh = cv.threshold(frame,thresh_hist,255,cv.THRESH_BINARY)
        return diff_thresh
class Value() :
    def __init__(self,treshold_hist=127):
        self.treshold_hist = treshold_hist
    def process(self,frame):
        _, diff_thresh = cv.threshold(frame,self.treshold_hist,255,cv.THRESH_BINARY)
        return diff_thresh
class StdTresh() :
    def __init__(self,factor=1.3):
        self.factor = factor    
    def process(self,frame):
        std = np.std(frame[frame>60])
        mean = np.mean(frame[frame>60])
        threshold = mean+3*std
        _, threshed_image = cv.threshold(frame,threshold,255,cv.THRESH_BINARY)
        print(f"mean {mean} , std {std}")
        return threshed_image
class Pourcent() :
    def __init__(self,pourcent=0.20):
        self.pourcent = pourcent
    def process(self,frame):
        max_frame = np.max(frame)
        _, threshed_image = cv.threshold(frame,max_frame*self.pourcent,max_frame,cv.THRESH_BINARY)
        return threshed_image
        
class KorniaSP():
    """
    Pseudo blob thresholding on GPU
    /!\ since this is based on a old kornia version, it might not work as expected

    Les différentes étapes du seuille sont :
    - Un filtrage par maximas locaux (on cherche les zones de maximas, cad des sortes de blobs)
    - Un filtrage avec la standard deviation 
    - Une erosion sur la sommation de ces deux filtrages
    - Une dilatation pour récupérer de plus gros points
    ...

    Attributes
    ----------
    kernel : tuple
        Taille du noyau pour l'extractions des maximas
    temperature : float
        Temperature de la fonction (à voir !)
    sigma : int
        Le nombre de sigma que l'on prend a partir du centre (mean), ce qui donne mean + sigma*std
    max_thresh : float
        Le pourcentage des maximas retenues (1-max_thresh)

    Methods
    -------
    process(additional=""):
        Prints the person's name and age.
    """

    def __init__(self,kernel=(7,7),temperature=5.0,sigma=3,max_thresh=0.2):
        self.temperature = temperature
        self.kernel = kernel
        pass
    def process(self,frame):
        """
        Seuillage pseudo "Blob-detector" sur GPU

        Attributes
        ----------
        frame : numpy.array
            Taille du noyau pour l'extractions des maximas
        """
        # On lit la frame sur le GPU
        data_cpu: torch.tensor = kornia.image_to_tensor(frame, keepdim=False)  # BxCxHxW
        data = data_cpu.float().to(0)

        # On récupère le mask des maxs et les maxes avec
        maxes = conv_soft_argmax2d(data, (7, 7), temperature=5.0, output_value=True)[1]
        maxes = maxes.squeeze()
        maxes = (maxes - maxes.min()) / (maxes.max() - maxes.min())
        maxes = maxes > 0.10
        data = data[..., 2:-2, 2:-2]
        data = data.squeeze()
        data_threshed = data.clone()
        data_threshed[~maxes] = 0

        # seuillage a 80
        # mask = data > 70
        mask = data > 60
        data_std_threshed = data.clone()
        # data_std_threshed[~mask] = 0
        # On recupère le mask avec la std et comme pour les maxs
        dmean = data_std_threshed[mask].cpu().mean()
        dstd = data_std_threshed[mask].cpu().std()
        # La std est utilisé comme valeur de seuillage
        thresh_value = (dmean).item()-dstd
        # thresh_value = 80
        print("mean %d std %d "%(dmean,dstd))
        print("tresh value : %d"% thresh_value)
        mask = data > thresh_value
        data_std_threshed = data.clone()
        data_std_threshed[~mask] = 0

        # On combine les deux cartes filtrés
        data_combine = data_std_threshed + data_threshed
        data_combine = data_combine > thresh_value
        data_combine = data_combine.float()

        # On termine par une dilatation qui permet de d'avoir de plus gros points
        open_struct = torch.ones(3, 3)
        # open_struct[:,-1] = 0
        # open_struct[-1,:] = 0

        dilation_struct = open_struct.to(0)
        # On externalise l'ouverture
        data_combine = opening(data_combine.unsqueeze(0).unsqueeze(0), dilation_struct)
        # open_struct = torch.ones(3, 3)
        # data_combine = open(data_combine.unsqueeze(0).unsqueeze(0), dilation_struct)
        # data_combine = data_combine.unsqueeze(0).unsqueeze(0)

        return data_combine.cpu().squeeze().numpy().astype(np.uint8)

class BlobDetection():
    def __init__(self,config_file="default.txt"):

        params = cv.SimpleBlobDetector_Params()
        
        params.filterByColor = False
        # params.filterByArea= True
        # params.filterByCircularity= False
        # params.filterByInertia= False
        # params.filterByConvexity= False
        # params.maxThreshold= 255
        # params.minThreshold= 20
        # params.minArea = 150
        # params.maxArea = 400
        # params.minRepeatability = 2
        params.maxThreshold= 127
        params.minThreshold= 5
        params.thresholdStep= 5
        params.minDistBetweenBlobs= 20
        params.filterByArea= True
        params.maxArea= 35
        params.minArea= 1.5
        params.filterByCircularity= True
        params.maxCircularity= 0.7
        params.minCircularity= 0.3
        params.filterByInertia= True
        params.maxInertiaRatio= 0.1
        params.minInertiaRatio= 0
        params.filterByConvexity= True
        params.maxConvexity= 1
        params.minConvexity= 0.5
        self.params = params
        self.detector = cv.SimpleBlobDetector_create(params)

    def process(self,frame):
        bg = np.zeros_like(frame,np.uint8)
        keypoints = self.detector.detect(frame)
        self._keypoints = keypoints
        print("Detected -> "+str(len(keypoints)))
        return bg
    @property
    def keypoints(self):
        return self._keypoints