import os
import sys
from ..utils.features import *
from .helpers import *
import otbApplication

def generate_rpc(input_points, file_output, elev_file="", geoid=False):
    'Generate RPCS from a list of points and a elevation file'
    app = otbApplication.Registry.CreateApplication(
        "GenerateRPCSensorModel")
    app.SetParameterString("outgeom", file_output)
    app.SetParameterString("outstat", "outputs/stats.geom")
    app.SetParameterString("inpoints", input_points)
    app.SetParameterString("map", "epsg")
    app.SetParameterInt("map.epsg.code", 4326)
    if len(elev_file) > 0:
        if geoid:
            print("USING GEOID")
            app.SetParameterString("elev.geoid", elev_file)
        else:
            print("USING DEM")
            app.SetParameterString("elev.dem", elev_file)
    else:
        print("NO ELEVATION SPECIFIED !")

    app.ExecuteAndWriteOutput()

def projection_gdalcmd(in_image, out_image, dem):
    """
    Warps the input image with rpcs/gcps/elevation file

    Attributes
    ----------
    in_image : str
        image input path
    out_image : str
        image output path
    dem : str
        The elevation file, for now only dted and tiff format worked

    Return
    ----------


    """
    cmd = 'gdalwarp -rpc -to RPC_DEM={rpcPath} -of GTiff {srcPath} {outPath} -overwrite -s_srs EPSG:4326 -t_srs EPSG:3857'\
        .format(srcPath=in_image,
                outPath=out_image,
                rpcPath=dem)
    print(f"COMMAND:\n{cmd}")
    return os.system(cmd)