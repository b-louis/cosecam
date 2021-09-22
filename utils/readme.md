# Utils

## Overview

This module contains useful functions/class, splited in two parts.

## Homography

This class is use for homography, for now only the global homography is implemented (**DLT; direct linear transform**).

### Example for Homography

```python
from cosecam.utils.homgraphy import * 
import cv2 as cv

img1 = cv.imread("my_image1.png")
img2 = cv.imread("my_image2.png")

homography = Homography()
# returns :
# img1_warp = img1
# img2_warp, img2 homgraphied to overlap img1
# `d` the distance below which matches are accepted
img1_warp, img2_warp = homography.global_homgraphy(img1, img2, d=0.7)
```



## Features

This module is composed of multiple features extraction methods used for various task (like homography), we can chose descriptors from :

- SIFT
- ORB
- AKAZE
- BRISK

And multiple matching algorithms :

- BruteForce
- Flann
- **Custom**

#### Custom matcher

This matcher uses a grid, in order to gain time. While using MSFS2020 generated images, we have some prior information on images.

We have the displacement between two frames, and we know that the plane only move in on direction only. So the images are only shifted on the x axis.

Having theses info allow us to match features locally which offer better performances.

### Example for features

```python
from cosecam.utils.features import * 
import cv2 as cv

# in this example we load two images
img1 = cv.imread("my_image1.png")
img2 = cv.imread("my_image2.png")

# with :
# kp1, the keypoints on the 1st image
# kp2, the keypoints on the 2nd image
# good, matches that respect the distance `d`
kp1,kp2,good = compute_features(img1,img2,mode=[Descriptors.SIFT, Matchers.FLANN],d=0.7)

```



> Written with [StackEdit](https://stackedit.io/).