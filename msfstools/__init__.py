import os
from .msfs_dec import Msfs_decoder
if os.name == 'nt':
    from .msfs_rec import Msfs_recorder