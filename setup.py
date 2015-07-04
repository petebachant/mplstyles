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
    stylelist = [f for f in os.listdir("./styles") \
                 if f.split(".")[-1] == "mplstyle"]
    if not os.path.isdir(styledir):
        os.makedirs(styledir)
    for s in stylelist:
        print("Copying {} to {}".format(s, styledir))
        s_local = os.path.join("./styles", s)
        shutil.copy2(s_local, os.path.join(styledir, s))
