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

Processes before we start detection

## Detection

Main detection, 

| name                 | description                                                  |
| -------------------- | ------------------------------------------------------------ |
| **Frame difference** | A basic method, difference between two frames                |
| **Weight Mean**      | Weighted frame difference, with three frames                 |
| **DP Mean**          | Implementation of [BGSLibrary's method](https://github.com/andrewssobral/bgslibrary/blob/master/src/algorithms/DPMean.cpp) |
| **Optical Flow**     | Farneback                                                    |

## Postprocess

Processes after detection

| name             | description                                                  |
| ---------------- | ------------------------------------------------------------ |
| **MedianFilter** | A basic method, difference between two frames                |
| **GaussFilter**  | Weighted frame difference, with three frames                 |
| **tree_filter**  | Implementation of [BGSLibrary's method](https://github.com/andrewssobral/bgslibrary/blob/master/src/algorithms/DPMean.cpp) |

## Thresholding



| name                | description                                                  |
| ------------------- | ------------------------------------------------------------ |
| **Cumsum**          | A basic method, difference between two frames                |
| **Value**           | Weighted frame difference, with three frames                 |
| **STD Tresholding** | Implementation of [BGSLibrary's method](https://github.com/andrewssobral/bgslibrary/blob/master/src/algorithms/DPMean.cpp) |
| **Pourcentage**     | Farneback                                                    |
| **KorniaSP**        | Farneback                                                    |

## Thresholding Postprocess

An additional process on thresholded image, for now there's just **Morphological Opening**

| name        | description                                                  |
| ----------- | ------------------------------------------------------------ |
| **Opening** | Morphological opening with a kernel (a 3x3 square by default) |

## Example

```python
from coscam.algorithms import * 

detector = detection.FrameDiff()
preprocessor = preprocess.PreProcessC()
postprocessor = postprocess.PostProcessC()
tresholder = tresholding.Value(127)
posttresholder = tresholding_postprocess.Opening()

# on fait le pre process
preprocessed_frame = preprocessor.process(frame)

# on effectue la detection
detection = detector.process(preprocessed_frame)

# on fait le post process
postprocessed_frame = postprocessor.process(detection)

# on fait le seuillage
thresholded_frame = tresholder.process(postprocessed_frame)

# on fait le seuillage
thresholded_frame = tresholding_postprocess.process(postprocessed_frame)
```



> Written with [StackEdit](https://stackedit.io/).
