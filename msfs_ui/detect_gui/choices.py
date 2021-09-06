import os,sys
sys.path.append(os.path.abspath('e:/Repos/cose-experiments/'))
from coscam.algorithms.detection import *
from coscam.algorithms.postprocess import *
from coscam.algorithms.preprocess import *
from coscam.algorithms.thresholding import *
from coscam.algorithms.thresholding_postprocess import *
detection_list = {
    "Weighted Mean":WeightMean,
    "Frame Difference":FrameDiff,
    "DPMean":DPMean,
    "OpticalFlow":OpticalFlow,
    }
preprocess_list = {
    "Median Filter":MedianFilter,
    "Gauss Filter":GaussFilter,
    "NoProcess":NoProcess,
    }
postprocess_list = {
    "Median and Dilate":MedianDilate,
    "NoProcess":NoProcess,
    }
threshold_list = {
    "Value":Value,
    "Pourcentage":PourcentageThresh,
    "Pourcentage of maximum":Pourcent,
    "Standard deviation":StdTresh,
    "Kornia custom":KorniaSP,
    }
threshold_postprocess_list = {
    "Opening":Opening,
    "NoProcess":NoProcess()
    }
detection_selected = {
    "Weighted Mean":[],
    "Frame Difference":FrameDiff(),
    "DPMean":[],
    "OpticalFlow":OpticalFlow(),
    }
preprocess_selected = {
    "Median Filter":[],
    "Gauss Filter":[],
    "NoProcess":NoProcess(),
    }
postprocess_selected = {
    "Median and Dilate":[],
    "NoProcess":NoProcess(),
    }
threshold_selected = {
    "Value":[],
    "Pourcentage":[],
    "Pourcentage of maximum":[],
    "Standard deviation":[],
    "Kornia custom":[],
    }
threshold_postprocess_selected = {
    "Opening":[],
    "NoProcess":NoProcess()
    }