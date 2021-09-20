# COSECAM
Cosecam is a python library for recording / orthorectification and detection on synthetic images from MSFS2020.
It's divided in 5 parts :

|  |  |
|--|--|
| ***[algorithms](algorithms/readme.md)*** | with all the detection/thresholding/processing algorithms  |
| ***[geo](geo/readme.md)*** |  with all the georeferencement/orthorectification  |
| ***[msfstools](msfstools/readme.md)*** | with all the MSFS2020 (Flight Simulator 2020), recording/decoding functions  |
| ***[utils](utils/readme.md)*** | with features and homography function |
| ***[config](config/readme.md)*** | config file  |


## Requirements

To setup the environment run :

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
Optionally export the `/OTB-7.3.0-Linux64/lib/python` into your `PYTHONPATH` variable into `~/.bashrc` so *otbApplication* is always importable from python.

## Known issues on installation

If you are using OTB python warpper with **PROJ>8.0** it wont work due to changes on *PROJ* database (*proj.db*). 

This library was only tested with *PROJ* = 7.0.0 and 6.2.1



```
ERROR 6: Unable to load EPSG support gcs.csv file check setting GDAL_DATA environment variable which point to gdal library contains EPSG.csv file
```

***GDAL_DATA*** environment variable have to be set correctly, set it to GDAL's data folder which contains `gcs.csv`. 

<u>Examples:</u>

In a *GDAL* independent install `D:\mygdal\data`

In *OTB* it's `D:\myotb\share\data`  

With a Anaconda *GDAL* it's `D:\Anaconda\Library\share\gdal`  



```
ERROR 1: PROJ: pj_obj_create: Cannot find proj.db
```

***PROJ_LIB*** environment variable have to be set correctly, set it to PROJ's data folder which contains `proj.db`.

 <u>Examples:</u>

In *OTB* it's `D:\myotb\share\proj`  

With a Anaconda *PROJ* it's `D:\Anaconda\Library\share\proj`  



```
ERROR 1: PROJ: proj_create_from_database: /home/[...]/proj.db lacks DATABASE.LAYOUT.VERSION.MAJOR / DATABASE.LAYOUT.VERSION.MINOR metadata. It comes from another PROJ installation.
ERROR 1: Translating source or target SRS failed:
```

This is due to different versions conflict. *PROJ* and *proj.db* are in different versions.

Change **PROJ_LIB** to the right version.



```
ERROR 1: PROJ: proj_create_from_database: [...] no such column: ***
```

Using a too recent version of *PROJ* will pop this error.

Install a *PROJ* version **<u>below</u>** 8.0.0



```
ERROR 6: EPSG PCS/GCS code 4326 not found in EPSG support files.  Is this a valid EPSG coordinate system?
ERROR 1: Translating source or target SRS failed:
```

Using a ***GDAL_DATA*** pointing to a different version of *GDAL* will pop this error. However, if we use *GDAL*=2.3.3 with ***GDAL_DATA*** pointing to data from *GDAL*=2.4.4 it works, but with data from  *GDAL*=3.0.0 it will not work


> Written with [StackEdit](https://stackedit.io/).
