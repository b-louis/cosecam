# COSECAM
Cosecam is a python library for recording / orthorectification and detection on synthetic images from MSFS2020.
It's divided in 5 parts :
|  |  |
|--|--|
| ***algorithms*** | with all the detection/thresholding/processing algorithms  |
| ***geo*** |  with all the georeferencement/orthorectification  |
| ***msfstools*** | with all the MSFS2020 (Flight Simulator 2020), recording/decoding functions  |
| ***utils*** | with features and homography fucntion  |
| ***config*** | config file  |


## Requirements

- GDAL
- Python
	- opencv
	- numpy
	- libgdal
	- imutils
	- skimage
	- kornia
	- torch
	- d3dshot
    - pyside2
- PIP
- CONDA

For recording :

- Windows 7 or + ( impossible on Unix systems )
- Flight Simulator 2020
- simconnect
- 2 screens for recording **(highly recommended)**


> Written with [StackEdit](https://stackedit.io/).
