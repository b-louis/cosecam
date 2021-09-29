import shutil
from osgeo import gdal, osr
import numpy as np
import os
# import matplotlib.pyplot as plt
import sys
from ..utils.features import *
from .helpers import *
if not os.name == 'nt':
    # Unusable on Windows OS (unless GDAL<3 and python = 3.5.*)
    from .gen_lin import *
else:
    from .gen_win import *
############# IMAGE GENERATION #############
def generate_input_tif(gcps, image_input, image_output, elev_file="", geoid=False):
    """
    Generates a GEOTIFF with georeferencement and rpc coeficients from an images and a list of points

    Attributes
    ----------
    gcps : list
        list of computed GCPS
    image_input : str
        image input path
    image_output : str
        image output path
    elev_file : str
        The elevation file, for now only dted and tiff format worked
    geoid : bool
        Enable or not the geoid flag. MUST be use with appropriate elev_file
    Return
    ----------


    """
    # temporary files /!\ better if each instance gets a generated name
    tmp_gcps = "tmp/tmp_gcps.txt"
    tmp_geom = "tmp/tmp_geom.geom"
    # Compute GCPS and save them for OTB format
    gcps_out, gcps_gdal = convert_save_gcps(gcps, tmp_gcps)
    # Compute RPCs no geoid no dem
    generate_rpc(tmp_gcps, tmp_geom, elev_file, geoid)
    # reading rpcs
    rpc, rpc_geom = readgeom(tmp_geom)
    # os.remove(tmp_geom)
    # os.remove(tmp_gcps)
    # Create a copy of the original file and save it as the output filename:
    shutil.copy(image_input, image_output)
    # Open the output file for writing :
    ds = gdal.Open(image_output, gdal.GA_Update)
    # Set spatial reference:
    sr = osr.SpatialReference()
    # 2193 refers to the NZTM2000, but can use any desired projection
    sr.ImportFromEPSG(4326)

    # Apply the GCPs to the open output file:
    ds.SetGCPs(gcps_gdal, sr.ExportToWkt())
    # No RPC (not working properly)
    ds.SetMetadata(rpc, 'RPC')

    # Close the output file in order to be able to work with it in other programs:
    ds = None
    #os.remove(image_input)


def convert_save_gcps(gcps, file_output):
    nb_points = gcps.shape[0]
    new_gcps = gcps.copy()
    new_gcps[:, -1] = 2400-new_gcps[:, -1]
    # 0:mapX 1:mapY 2:pixelX 3:pixelY
    gcps_gdal = [gdal.GCP(new_gcps[i][0], new_gcps[i][1], 0,
                          new_gcps[i][2], new_gcps[i][3]) for i in range(nb_points)]
    header = ['pixelX', 'pixelY', 'mapX', 'mapY']
    header_save = ','.join(header)
    np.savetxt(file_output, new_gcps[:, [
               2, 3, 0, 1]], header=header_save, fmt='%f')
    return new_gcps, gcps_gdal


def readgeom(file_input):
    'Reads and parses rpcs from a geom file (OTB)'
    f = open(file_input)
    values = f.readlines()
    f.close()
    rpc_geom = dict(map(lambda x: x.replace(
        "\n", "").replace(" ", "").split(':'), values))
    line_den_coeff_geom = [rpc_geom['line_den_coeff_%i' % i]for i in range(20)]
    line_num_coeff_geom = [rpc_geom['line_num_coeff_%i' % i]for i in range(20)]
    samp_den_coeff_geom = [rpc_geom['samp_den_coeff_%i' % i]for i in range(20)]
    samp_num_coeff_geom = [rpc_geom['samp_num_coeff_%i' % i]for i in range(20)]
    rpc = [
        "HEIGHT_OFF="+(rpc_geom['height_off']),
        "HEIGHT_SCALE="+(rpc_geom['height_scale']),
        "LAT_OFF="+(rpc_geom['lat_off']),
        "LAT_SCALE="+(rpc_geom['lat_scale']),
        "LINE_DEN_COEFF="+(' '.join(line_den_coeff_geom)),
        "LINE_NUM_COEFF="+(' '.join(line_num_coeff_geom)),
        "LINE_OFF="+(rpc_geom['line_off']),
        "LINE_SCALE="+(rpc_geom['line_scale']),
        "LONG_OFF="+(rpc_geom['long_off']),
        "LONG_SCALE="+(rpc_geom['long_scale']),
        "SAMP_DEN_COEFF="+(' '.join(samp_den_coeff_geom)),
        "SAMP_NUM_COEFF="+(' '.join(samp_num_coeff_geom)),
        "SAMP_OFF="+(rpc_geom['samp_off']),
        "SAMP_SCALE="+(rpc_geom['samp_scale'])
    ]
    return rpc, rpc_geom

############# IMAGE GENERATION #############