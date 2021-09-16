from cdcosecam.geo.georef import *
from cosecam.msfstools.msfs_rec import *

# digital elevation file
dem_file = "/home/user/DTEDS/N40E01.dted"
# setting images, getting the center for Steregcp calculation
dec = Msfs_decoder("/home/user/datasets/","exemple")
center = dec.getResolution()/2

# you can chose the type of descriptor and matching algorithms for GCP generation
mode = [Descriptors.SIFT,Matchers.FLANN]
# the discriminating distance
d = 0.1 

# initialize all classes
gcp_gen = StereoGCP(center)
rpc_gen = RpcGenerator(dem_file)
orthorect = OrthoRectification(projection_gdalcmd,dem_file)

# we create the main object, that compute the whole 
geo = Georeferencer(gcp_gen,rpc_gen,orthorect,d=d,mode=mode)

# when we setDataset, we set the dataset object and 
# the orthorectification folder output
geo.setDataset(dec,"/home/user/datasets/example1_orthorectified/")

# it computes all images in the folder
geo.run()