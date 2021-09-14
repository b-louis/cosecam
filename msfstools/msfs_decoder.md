# Msfs decoder
This module reads saved dataset (from MSFS recorder).

## Overview 
The class, **Msfs_decoder** reads all datas from two files :
- **values.txt** that contains plane related values at each time (gps position, heading,...)
- **images.txt** that contains all the images path, the number of images and entries values is the same.

**Msfs_decoder** implements iterator's method and **\_\_getitem\_\_** to access data more easily.

Values that are **None** in **values.txt** are interpolated, for example if we have :

|  1   | None | None | None |  2   |
| :--: | :--: | :--: | :--: | :--: |

we will get :

|  1   | 1.25 | 1.5  | 1.75 |  2   |
| :--: | :--: | :--: | :--: | :--: |



## Parameters
| name | description |
|--|--|
| **root_folder** | *str* : root dataset folder |
| **folder_name** | *str* : dataset folder |
| **only_path** | *bool* : whenever a image is returned when we acces to a data <br> default : **False** |
| **only_images** | *bool* : whenever planes values are returned when we acces to a data <br> default : **False** |

## Functions
| name | parameters| description  |
|--|--|--|
| **getAll** |*str* : value_name <br> The value field we want to get |return all values from one value field  |
| **getResolution** |  |return the image resolution|

## Data structure

Same as [msfs_recorder](msfs_recorder.md)

## Notes

### Returned entries 
Entries are return in different forms with the ***only_path*** and ***only_images*** parameters. 
When both are **False**, we get a dictionary like  :

>*{'image' : np.array([....]), 'values' : np.array([....])}*

When only ***only_path*** is **False**, we get a dictionary like  :
>*{'image' : "/home/alldatasets/mydataset/000.png", 'values' : np.array([....])}*

When only ***only_images*** is **False**, we get the image as an output  :
>np.array([....])

When both are **True**, we get a *string* of the image path   :
>"/home/alldatasets/mydataset/000.png"

### Attributes
|name  | description |
|--|--|
| **units** | Recorded simvars units  |
| **vars** | Recorded simvars names |
| **number_images** | number of recorded images |



## Example
```python
from coscam.msfstools.msfs_dec import *
dec = Msfs_decoder("/mnt/plus/images_database/","3400ft_netherland")
entry_1 = dec[1]
#return > {'image' : np.array([....]), 'values' : np.array([....])}
image = entry_1["image"]
# return > np.array([ 0 , 125 , 255....])
value= entry_1["value"]
# return > {"PLANE_ATTITUDE" : 49.54668434,....}
value= entry_1["value"]["PLANE_ATTITUDE"]
# return > 49.54668434
print(dec.getAll("PLANE_ATTITUDE"))
# return > np.array([48.54668434, 49.54668434, ....])

```

## Known issues

Nothing
> Written with [StackEdit](https://stackedit.io/).
