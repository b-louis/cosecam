import time
import imutils
import os
import sys
import numpy as np
import cv2 as cv
# TODO: 
# Less repitions in code
class Msfs_img_only_decoder:
    
    '''
    Reading images from txt files 
    '''

    def __init__(self, root_folder: str, folder_name: str,):
        self.root_folder = root_folder
        self.folder_name = folder_name
        self.n = 0

        f_images = root_folder + "/" + folder_name + "/images.txt"
        f_i = open(f_images)
        try:
            self.images = np.loadtxt(f_i, skiprows=2, delimiter=",", dtype=str)
            self.number_images = len(self.images)
        except Exception:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        f_i.close()

    def __getitem__(self, key: int):
        return cv.imread(self.root_folder + "/" + self.images[key])

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.number_images:
            out = self[self.n]
            self.n += 1
            return out
        else:
            raise StopIteration

    def initial_image(self):
        return self[0]

    def next_image(self):
        if self.n < self.number_images:
            self.n += 1
        return self[self.n]

    def previous_image(self):
        if 0 < self.n:
            self.n -= 1
        return self[self.n]

    @property
    def current_frame(self):
        return self.n

class Msfs_path_decoder:
    '''
    Reading path and values from txt to orthorectifiction 
    '''

    def __init__(self, root_folder: str, folder_name: str,):
        self.root_folder = root_folder
        self.folder_name = folder_name
        self.n = 0

        f_images = root_folder + "/" + folder_name + "/images.txt"
        f_i = open(f_images)
        try:
            self.images = np.loadtxt(f_i, skiprows=2, delimiter=",", dtype=str)
            self.number_images = len(self.images)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        f_i.close()

    def __getitem__(self, key: int):
        return cv.imread(self.root_folder + "/" + self.images[key])

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.number_images:
            out = self[self.n]
            self.n += 1
            return out
        else:
            raise StopIteration

    def initial_image(self):
        return self[0]

    def next_image(self):
        if self.n < self.number_images:
            self.n += 1
        return self[self.n]

    def previous_image(self):
        if 0 < self.n:
            self.n -= 1
        return self[self.n]

    @property
    def current_frame(self):
        return self.n
class Msfs_decoder:
    '''
    Reading images and values from txt files 
    '''

    def __init__(
        self,
        root_folder,
        folder_name,
        only_path=False,
        only_images=False,
        ):
        
        self.only_path = only_path
        self.only_images = only_images
        self.root_folder = root_folder
        self.folder_name = folder_name
        if self.only_images:
            self._only_img_init()
        else:
            self._full_init()
    def _full_init(self):
        def map_split(x):
            return x.split(',')
        def pad(input_data):
            """
                For 'None' data filling.
                Sometimes we get 'None' value during recording, this function interpolates these values
            """
            # source : https://stackoverflow.com/questions/6518811/interpolate-nan-values-in-a-numpy-array 
            data = input_data.copy()
            bad_indexes = np.isnan(data)
            good_indexes = np.logical_not(bad_indexes)
            good_data = data[good_indexes]
            interpolated = np.interp(bad_indexes.nonzero()[0], good_indexes.nonzero()[0], good_data)
            data[bad_indexes] = interpolated
            return data
        def load2dict(keys,x):
            return dict(zip(keys,x))
        self.n = 0
        f_values = self.root_folder + "/" + self.folder_name + "/values.txt"
        f_images = self.root_folder + "/" + self.folder_name + "/images.txt"
        f = open(f_values)
        f_i = open(f_images)
        try:
            a = f.read().replace('None','nan').splitlines()

            # first 5 lines are units,number of images and captured simvars
            self.units = a[-4].replace("'",'').split(',') + a[1].replace("'",'').split(',')
            self.number_images = int(a[3])
            
            self.vars = a[4].replace("'",'').replace(" ",'').split(',')
            self.vars_be = a[-3].replace("'",'').replace(" ",'').split(',')

            keys = self.vars_be + self.vars

            values = list((map(map_split,a[5:-5])))
            values = np.array(values,dtype=float)
            values = np.apply_along_axis(pad, 0, values)

            values_end = list((map(map_split,a[-2:])))
            values_end = np.array(values_end,dtype=float)
            values_end = values_end.mean(0)
            values_end = np.tile(values_end, (self.number_images, 1))

            # we open the imagefile with file paths
            self.images = np.loadtxt(f_i, skiprows=2, delimiter=",", dtype=str)

            # we add the mean values of the simvars that are taken 2 times
            # at the beginning and at the end
            self.values = np.concatenate((values_end, values), axis=1)

            # convert values and units to a dict for more readability
            self.values = list(map(lambda x : load2dict(keys,x),self.values))
            self.units = dict(zip(keys,self.units))

            # set image' scale (TO CHANGE !)
            self.pix_scale = 100/200 #(1/2 pixel for 1meter)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        f.close()
        f_i.close()

    def _only_img_init(self):
        self.n = 0

        f_images = self.root_folder + "/" + self.folder_name + "/images.txt"
        f_i = open(f_images)
        try:
            self.images = np.loadtxt(f_i, skiprows=2, delimiter=",", dtype=str)
            self.number_images = len(self.images)
        except Exception:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        f_i.close()

    def __getitem__(self, key: int):
        if not self.only_path:
            out = cv.imread(self.root_folder + "/" + self.images[key])
        else:
            out = self.root_folder + "/" + self.images[key]
        if self.only_images:
            return out
        return {'image':out, 'values':self.values[key]}

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.number_images:
            out = self[self.n]
            self.n += 1
            return out
        else:
            raise StopIteration

    def initial_image(self):
        return self[0]

    def next_image(self):
        if self.n < self.number_images:
            self.n += 1
        return self[self.n]

    def previous_image(self):
        if 0 < self.n:
            self.n -= 1
        return self[self.n]
    
    def getAll(self,value_name):
        return np.array([item[value_name] for item in self.values])
    def getResolution(self):
        if self.only_path:
            print('unavaliable, must be open in image only mode or full mode')
        elif self.only_images:
            return self[0].shape[:2]
        return np.array(list(self[0]['image'].shape[:2][::-1])).astype(int)
    @property
    def current_frame(self):
        return self.n