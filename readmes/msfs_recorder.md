# Msfs recorder
This module is use to record images from *Flight Simulator 2020*, with the plane's values in parallel.
## Overview 
The class, **Msfs_recoder** reads all datas from two files :
- **values.txt** that contains plane related values at each time (gps position, heading,...)
- **images.txt** that contains all the images path, the number of images and entries values is the same.

**Msfs_decoder** implements iterator's method and **\_\_getitem\_\_** to access data more easily.

Values that are **None** in **values.txt** are interpolated, 
## Parameters
| name | description |
|--|--|
| **rootfolder** | str : dataset rootfolder |
| **dataset_name** | str : dataset name, this is the dataset's folder name |
| **d3d** | object: d3dshot object |
| **nb_images** | int: number of recorded images, ***100*** by default |
| **output_type** | str : type of output, ***png*** by default  |
| **fps** | int : recording frame rate, ***1*** by default |

## Configuration
**The game doesn't converts units well ( as 27/07/2021 ) keep *feets* and *kts*.**

If you have a 2 screen setup, the game launches on the **primary screen**.
In case you need a higher output resolution you can tweak the ***DLSS*** parameter in Nvidia control panel, resolution will be changed only on the primary screen

If you don't use QT interface, it's better to pre-write your script before you start the game.
### Qt interface :

##image##
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
- with the QT interface
- with a python script

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
### STEPS
After you launch the game, you have to :

1. Chose 'Flight'
2. To chose a route, there's multiple ways
	
	- You can do a *right click* on and select your departure position and your arrival 
	- You also can *click* on the existing points of interest, 
		>Be careful by selecting a existing point, you can end up in a position with no speed etc (à revoir !)
		
	- Or You can select them from the search bar
3. Chose your flight attitude in *navigation journal*
	>  Be careful (as 27/07/2021) the attitude doesn't account landforms, you can end up too close to the ground.

4. Select weather condition (can be changed via dev panel)
5. Select your plane (the cruising speed is different from one another)
6. Launch your flight, at the end of the loading, the game doesn't start directly it's paused. Press 'Resume??' 
**The plane is on your control at the beginning, you have to set AI pilot first**
7. Menus are hidden unless you move your mouse, press **'Pause'** button.
8. Then select the **Control** section and check **AI pilot**
**Now you have to set your camera**
10. Go to **Camera** section and set 
11. put on pause
12. camera
13. remove all windows between the game and your screen 
14. Launch your script


## Known issues
Capture time can have a variable offset. This is due to two factors.

Firstly, if your game is running at a low frame rate, your computer will run slower too and have much more difficulty to take values at the right time. 

Then, the way *SimVars* are retrieve, they are taken sequentially even when we have a lot of them. Some value that couldn't be capture at right time will be assign to *None*.

For now, the pixel size is hard coded, 
```python
# set image' scale (TO CHANGE !)
self.pix_scale = 100/200  #(1/2 pixel for 1meter)
```
In case you have images that have a dif
