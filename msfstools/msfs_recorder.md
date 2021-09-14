# Msfs recorder
This module is use to record images from *Flight Simulator 2020*, with the plane's values in parallel.
## Overview 
The class, **Msfs_recoder** saves all images and saves two files :
- **values.txt** that contains plane related values at each time (gps position, heading,...)
- **images.txt** that contains all the images path, the number of images and entries values is the same.

## Parameters
| name | description |
|--|--|
| **rootfolder** | str : dataset rootfolder |
| **dataset_name** | str : dataset name, this is the dataset's folder name |
| **d3d** | object: d3dshot object |
| **nb_images** | int: number of recorded images, ***100*** by default |
| **output_type** | str : type of output, ***png*** by default  |
| **fps** | int : recording frame rate, ***1*** by default |

## Data structure

Images are save as **000.png**, **001.png**,...

For example, we can use ***rootfolder* = "datasets"** and ***dataset_name* = example1 ** 

```
.
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
    └── example2/
        ├── 000.png
        ├── 001.png
        ├── 002.png
        ├── 003.png
        ├── values.txt
        └── images.txt
```



## Configuration

**The game doesn't converts units well ( as 27/07/2021 ) keep *feets* and *kts*.**

If you have a 2 screen setup, the game launches on the **primary screen**.
In case you need a higher output resolution you can tweak the ***DLSS*** parameter in Nvidia control panel, resolution will be changed only on the primary screen

If you don't use QT interface, it's better to pre-write your script before you start the game.
### Qt interface :

![Recorder gui](..\images\rec_gui_editr.png)
1. root folder is the main folder containing all your saved dataset
2. dataset's name
3. all the values that are taken during the whole recording
4. all the values that are only taken at the beginning and the end
5.  fps
6. number of saved images
7. image format
8. not implemented
9. run button to start recording
## How-to
There's two ways to run the recording:
- with the QT interface, ([tutorial here](msfs_recorder_howto.md))
- with a python script

###### A python script example

```python
from coscam.msfstools.msfs_rec import *
d3d = d3dshot.create(capture_output="numpy")
# parameters are :
# rootfolder,
# dataset_name,
# nb_images,
# output_type,
# fps
rec = Msfs_recorder(".","mountain_1",d3d,100,"png",3)
rec.run()
```



## Known issues
Capture time can have a variable offset. This is due to two factors.

Firstly, if your game is running at a low frame rate, your computer will run slower too and have much more difficulty to take values at the right time. 

Then, the way ***SimVars*** are retrieve, they are taken sequentially even when we have a lot of them. Some value that couldn't be capture at right time will be assign to ***None***.

For now, the pixel size is hard coded, 

```python
# set image' scale (TO CHANGE !)
self.pix_scale = 100/200  #(1/2 pixel for 1meter)
```

In case you have images that have a different pixel scale, you need to change this value in this [file](../msfstools/msfs_rec.py)
