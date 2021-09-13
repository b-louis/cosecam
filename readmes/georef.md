
# Geo

This part of the application is used for orthorectification.
Before going further be sure you have set your environment correctly ##href##.
>Note that it still very rough, some features aren't implemented (those with a '*').
## Overview
This module is use to do the whole orthorectification from a non georeferenced image with GPS values at center to a orthorectified image (georeferenced or not)

## Functions
|  |  |
|--|--|
| coords_distance |  |
| cal_lat_lon|  |
| angle_from_coord|  |
| load_gcps|  |
| generate_input_tif|  |
| convert_save_gcps|  |
| readgeom |  |
| generate_rpc|  |
| projection_gdalcmd|  |
## Classes
|  |  |
|--|--|
| StereoGCP|  |
| RpcGenerator|  |
| OrthoRectification|  |
| Georeferencer|  |
## Exemple

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
You can use *[OTBApplication](https://www.orfeo-toolbox.org/CookBook/PythonAPI.html)* instead, but for now we still use *gdalwarp* on cli mode

