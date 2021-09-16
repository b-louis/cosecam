import os
from .msfs_rec import Msfs_recorder
if os.name == 'nt':
    from .msfs_dec import Msfs_decoder