#!/usr/bin/env python
"""
This script copies the mplstyles in this directory to the user's 
`mpl_config/stylelib` directory.

"""
from __future__ import print_function
import sys
import shutil
import os
import matplotlib

if sys.argv[1] == "install":
    configdir = matplotlib.get_configdir()
    styledir = os.path.join(configdir, "stylelib")
    stylelist = ["arial", "latex", "ggplot-mod", "times"]
    stylelist = [s + ".mplstyle" for s in stylelist]
    if not os.path.isdir(styledir):
        os.makdirs(styledir)
    for s in stylelist:
        print("Copying {} to {}".format(s, styledir))
        shutil.copy2(s, os.path.join(styledir, s))
