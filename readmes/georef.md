
# Geo

This part of the application is used for orthorectification.
Before going further be sure you have set your environment correctly (see [requierements](../README.MD))

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
| **Georeferencer** | Main class for the whole process |

## Example

```python
dem_file = "/home/user/DTEDS/N40E01.dted"
dec = Msfs_decoder("/home/user/datasets/","exemple")
center = dec.getResolution()/2
gcp_gen = StereoGCP(center)
rpc_gen = RpcGenerator(dem_file)
orthorect = OrthoRectification(projection_gdalcmd,dem_file)
# we create the
geo = Georeferencer(gcp_gen,rpc_gen,orthorect)
geo.setDataset(dec,"/home/user/datasets/exemple_orthorectified/")
geo.run()
```

## Installation issues

There is some issues with *GDAL/OTB* that we encounter during our setup.

### On windows : 

There's issues with the different versions of *GDAL* in , a conflict can occur with *OTB/ANACONDA-PYTHON* version.

We use the command line method because OTB's python warpper don't work with python versions above *3.5.x*

In that case you'll need to change the **projection_gdalcmd** function:
```python 
cmd = 'E:/OTB-7.3.0-Win64/bin/gdalwarp.exe -rpc -to RPC_DEM={rpcPath} -of GTiff {srcPath}  {outPath} -overwrite -s_srs EPSG:4326 -t_srs EPSG:3857 '\
.format(srcPath=in_image,outPath=out_image,rpcPath=dem)

print(f"COMMAND:\n{cmd}")
```
Replace **E:/OTB-7.3.0-Win64/bin/gdalwarp.exe** with your gdalwarp path.

### On Linux: 
You can use *[OTBApplication](https://www.orfeo-toolbox.org/CookBook/PythonAPI.html)* instead, but for now it still uses *gdalwarp* on CLImode

