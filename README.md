# COSECAM
Cosecam is a python library for recording / orthorectification and detection on synthetic images from MSFS2020.
It's divided in 5 parts :

|  |  |
|--|--|
| ***[algorithms](algorithms/readme.md)*** | with all the detection/thresholding/processing algorithms  |
| ***[geo](geo/readme.md)*** |  with all the georeferencement/orthorectification  |
| ***[msfstools](msfstools/readme.md)*** | with all the MSFS2020 (Flight Simulator 2020), recording/decoding functions  |
| ***[utils](utils/readme.md)*** | with features and homography fucntion  |
| ***[config](config/readme.md)*** | config file  |


## Requirements

To setup the environement run :
`conda env create -f environment.yaml` 

If you are using a unix-based system run instead :
`conda env create -f env-unix.yaml`

Note that you may need to change the path to the env in the config file. 

## OTB installation
[OrfeoToolBox](https://www.orfeo-toolbox.org/) has to be installed as orthorectification uses this library. To install it, refer to [OTB documentation](https://www.orfeo-toolbox.org/CookBook/Installation.html).

> Written with [StackEdit](https://stackedit.io/).
