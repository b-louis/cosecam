import os
if os.name == 'nt':
    __all__ = ["msfs_rec", "msfs_dec"]
else:
    __all__ = ["msfs_rec"]
