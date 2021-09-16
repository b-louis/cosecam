import os
import sys
from ..utils.features import *
from .helpers import *

def generate_rpc(
        input_points,
        file_output,
        elev_file="",
        geoid=False):
    """
    Generate RPCS from a list of GCPS and a elevation file

    Attributes
    ----------
    gcps : list
        list of computed GCPS
    input_points : str
        points input path
    file_output : str
        geom output path, it's the file that contains the rpcs
    elev_file : str
        The elevation file, for now only dted and tiff format worked
    geoid : bool
        Enable or not the geoid flag. MUST be use with appropriate elev_file
    Return
    ----------


    """
    cmd = 'otbcli_GenerateRPCSensorModel -outgeom {file_output} -outstat {outstat} -inpoints {inpoints} "-map.epsg.code" 4326 -map "epsg" '\
        .format(
            file_output=file_output,
            outstat="stats.geom",
            inpoints=input_points,
        )
    print(cmd)
    if len(elev_file) > 0:
        if geoid:
            print("USING GEOID")
            cmd += "-elev.geoid "+str(elev_file)
        else:
            print("USING DEM")
            cmd += "-elev.dem "+str(elev_file)
    else:
        print("NO ELEVATION SPECIFIED !")
    print(f"COMMAND:\n{cmd}")
    return os.system(cmd)

def projection_gdalcmd(
        in_image,
        out_image,
        dem):
    """
    Warps the input image with rpcs/gcps/elevation file and outputs an orthorectified/georeferenced image file

    Attributes
    ----------
    in_image : str
        image input path
    out_image : str
        image output path
    dem : str
        The elevation file, for now only dted and tiff format worked

    ----------


    """
    # replace E:/OTB-7.3.0-Win64/bin/gdalwarp.exe with your otb's gdalwarp path
    cmd = 'gdalwarp -rpc -to RPC_DEM={rpcPath} -of GTiff {srcPath} {outPath} -overwrite -s_srs EPSG:4326 -t_srs EPSG:3857 '\
        .format(srcPath=in_image,
                outPath=out_image,
                rpcPath=dem)
    print(f"COMMAND:\n{cmd}")
    return os.system(cmd)