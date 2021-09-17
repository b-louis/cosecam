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

### Windows
`conda env create -f environment.yaml` 


## OTB installation
[OrfeoToolBox](https://www.orfeo-toolbox.org/) has to be installed as orthorectification uses this library. To install it, refer to [OTB documentation](https://www.orfeo-toolbox.org/CookBook/Installation.html).


### Linux
If you are using a unix-based system run instead :
```
conda env create -f env-unix.yaml
conda activate cosecam
cd OTB/install/directory
wget https://www.orfeo-toolbox.org/packages/archives/OTB/OTB-7.3.0-Linux64.run
chmod+x OTB-7.3.0-Linux64.run
./OTB-7.3.0-Linux64.run
cd OTB-7.3.0-Linux64
source otbenv.profile
ctest -S share/otb/swig/build_wrapping.cmake -VV
ln -s /home/pierre/miniconda3/envs/cosecam/lib/libpython3.9.so.1.0 lib/libpython3.9.so.1.0
```
Optionnaly export the `/OTB-7.3.0-Linux64/lib/python` into your `PYTHONPATH` variable into `~/.bashrc` so otbApplication is always importable from python.


> Written with [StackEdit](https://stackedit.io/).
