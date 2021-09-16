
# Geo

This part of the application is used for orthorectification. This module is splitted in 3 parts :

| *name*       | *description*                               |
| ------------ | ------------------------------------------- |
| **georef**   | Contains all classes for orthorectification |
| **helpers**  | Some function that facilitates computation  |
| **imagegen** | Functions for writting the output image     |

Before going further be sure you have set your environment correctly (see [requierements](../README.md))

>Note that it still very rough, some features aren't implemented (those with a '*').
## Overview
This module is use to do the whole orthorectification from a non georeferenced image with GPS values at center to a orthorectified image (georeferenced or not)

## Functions
| *functions*            | *description* |
|:--|:--|
| **coords_distance** | Computes the distance between on earth's surface |
| **cal_lat_lon** | Computes the longitude and latitude from a point with distance and angle |
| **angle_from_coord** | Computes the angle between true north and a point |
| **load_gcps** | Loads *GCPs* from a file and parses them in a *numpy.array* |
| **generate_input_tif** | Generates a georeferenced image from image, a list of *GCPs* and a elevation map |
| **convert_save_gcps** | Converts the *GCPs* format for *GDAL* |
| **readgeom** | Reads a *geom* file and parses it in *numpy.array* |
| **generate_rpc** | Generates *RPCs* with a list of points |
| **projection_gdalcmd** | *gdalwarp*  CLI function warpper in python |

## Classes
| *classes* | *description* |
|:--|:-|
| **StereoGCP**          | Class that generates *GCPs* |
| **RpcGenerator** | Class that generates *RPCs* |
| **OrthoRectification** | Class for orthorectification calculation |
| **Georeferencer** | Main class for the whole process, <br>computes all images within the specified folder |

## Example

```python
from cosecam.geo import *
from cosecam.msfstools.msfs_dec import *
from cosecam.utils.features import Descriptors,Matchers

# digital elevation file
dem_file = "/home/user/DTEDS/N40E01.dted"
# setting images, getting the center for Steregcp calculation
#dec = Msfs_decoder("/home/user/datasets/","exemple")

center = dec.getResolution()/2

# you can chose the type of descriptor and matching algorithms for GCP generation
mode = [Descriptors.SIFT,Matchers.FLANN]
# the discriminating distance
d = 0.1 

# initialize all classes
gcp_gen = StereoGCP(center)
rpc_gen = RpcGenerator(dem_file)
orthorect = OrthoRectification(projection_gdalcmd,dem_file)

# we create the main object, that compute the whole 
geo = Georeferencer(gcp_gen,rpc_gen,orthorect,d=d,mode=mode)

# when we setDataset, we set the dataset object and 
# the orthorectification folder output
geo.setDataset(dec,"/home/user/datasets/example1_orthorectified/")

# it computes all images in the folder
geo.run()
```

## Data structure

See  [msfs_recorder](msfs_recorder.md) for input data structure.

The output structure is : 

```.
└── datasets/
    ├── example1/
    │   ├── 000.png
    │   ├── 001.png
    │   ├── 002.png
    │   ├── 003.png
    │   ├── 004.png
    │   ├── 005.png
    │   ├── values.txt
    │   └── images.txt
    └── example1_orthorectified/
        ├── 000.png
        ├── 001.png
        ├── 002.png
        ├── 003.png
        ├── 004.png
        ├── 005.png
        ├── values.txt
        └── images.txt
```

Output images are orthorectified, not georeferenced and homographied by pairs .

Example : **000.png** is homographied with **001.png**, and **002.png** is homographied with **003.png**  but **000.png** are not **002.png**

## Installation issues

There is some issues with *GDAL/OTB* that we encounter during our setup.

### On windows : 

We are force to use CLI because *OTB's python* warpper doesn't work with python versions above *3.5.x*

There's issues when different versions of *GDAL* are in conflict (the *OTB's* GDAL and  *ANACONDA-PYTHON's* version).

It's solvable by reinstalling *python's gdal*/libgdal (via conda) or by using the command line method on *OTB's* directory. 

In that case you'll need to change the **projection_gdalcmd** function:
```python 
cmd = 'E:/OTB-7.3.0-Win64/bin/gdalwarp.exe -rpc -to RPC_DEM={rpcPath} -of GTiff {srcPath}  {outPath} -overwrite -s_srs EPSG:4326 -t_srs EPSG:3857 '\
.format(srcPath=in_image,outPath=out_image,rpcPath=dem)

print(f"COMMAND:\n{cmd}")
```
Replace **E:/OTB-7.3.0-Win64/bin/gdalwarp.exe** with your gdalwarp path.

### On Linux: 
You can use *[OTBApplication](https://www.orfeo-toolbox.org/CookBook/PythonAPI.html)* instead, but for now it still uses *gdalwarp* on CLImode

