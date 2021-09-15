# Algorithms
This module contains all the algorithms for detection.
It's divided in five independent parts :

|  |  |
|--|--|
| ***preprocess*** | image preprocessing functions (such as median filter)  |
| ***detection*** | all detection algorithms  |
| ***postprocess*** |  post process functions on the raw detection image  |
| ***thresholding*** | thresholding functions  |
| ***thresholding_postprocess*** | post process on thresholded image  |

## Preprocess

Processes before we start detection, takes a image as input and return an image too.

| name             | description                                                  |
| ---------------- | ------------------------------------------------------------ |
| **MedianFilter** | A [median filter](https://en.wikipedia.org/wiki/Median_filter) |
| **GaussFilter**  | A [gaussian filter](https://en.wikipedia.org/wiki/Gaussian_blur) |
| **tree_filter**  | A tree filter, that discriminates on pixel's HSV color       |

## Detection

Main detection, all these method takes a ***list*** of frames and returns a detection images

| name                 | description                                                  |
| -------------------- | ------------------------------------------------------------ |
| **Frame difference** | A basic method, difference between two frames                |
| **Weight Mean**      | Weighted frame difference, with three frames                 |
| **DP Mean**          | Implementation of [BGSLibrary's method](https://github.com/andrewssobral/bgslibrary/blob/master/src/algorithms/DPMean.cpp) |
| **Optical Flow**     | Farneback optical flow                                       |

## Postprocess

Processes after detection, takes a image as input and return an image too.

| name             | description                                                  |
| ---------------- | ------------------------------------------------------------ |
| **MedianDilate** | A median filter then a dilatation. The objective is to enhance points to get bigger responses (like blobs) |

## Thresholding

Takes a detection image as input and return a thresholded image.

| name                | description                                                  |
| ------------------- | ------------------------------------------------------------ |
| **Cumsum**          | Takes the cumulative sum histogram, and uses slope's<br>gradient as a threshold value |
| **Value**           | Uses a fixed threshold value                                 |
| **STD Tresholding** | Models the histogram as a standard deviation and looks for <br>values above **µ + 3*σ** |
| **Pourcentage**     | Uses a pourcentage of the maximum as threshold a value       |
| **KorniaSP**        | A method that combines **STD Tresholding** with a pseudo blob detection |

## Thresholding Postprocess

An additional process on thresholded image, for now there's just **Morphological Opening**, takes a image as input and return an image.

| name        | description                                                  |
| ----------- | ------------------------------------------------------------ |
| **Opening** | Morphological opening with a kernel (a 3x3 square by default) |

## Data structure

Input are [geo's output](../geo/readme.md)

## Example

```python
from coscam.algorithms import * 
import cv2 as cv

detector = detection.FrameDiff()
preprocessor = preprocess.PreProcess(mode="median",size=3)
postprocessor = postprocess.PostProcessC()
tresholder = tresholding.Value(127)
posttresholder = tresholding_postprocess.Opening()

# in this example we load two images, but we can use a video output too
# by taking multiple succesives images 
img1 = cv.imread("my_image1.png")
img2 = cv.imread("my_image2.png")
frames = [img1,img2]

preprocessed_frame = preprocessor.process(frames)

detection = detector.process(preprocessed_frames)

postprocessed_frame = postprocessor.process(detection)

thresholded_frame = tresholder.process(postprocessed_frame)

thresholded_frame = tresholding_postprocess.process(postprocessed_frame)

cv.imshow("final image",thresholded_frame)
```



> Written with [StackEdit](https://stackedit.io/).
