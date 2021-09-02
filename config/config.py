
"""
All saved variables from MSFS, there is 2 types:
    - VARS that are taken at each steps
    - VARS_BEGIN_ENS are only taken at the beginning and the end
It's the same for the units (they are linked to vars)
"""

# TODO:
# Cleaner code
# Add name indexing for values

VARS = [
    "PLANE_ALT_ABOVE_GROUND",
    "PLANE_LATITUDE",
    "PLANE_LONGITUDE",
    "TIME"
]

VARS_BEGIN_END = [
    "PLANE_ALTITUDE",
    "AIRSPEED_INDICATED",
    "HEADING_INDICATOR",
]

UNITS = ["FEETS", "DEGREES", "DEGREES", "SECONDS"]
UNITS_BEGIN_END = ["FEETS", "KNOTS", "RADIANS"]