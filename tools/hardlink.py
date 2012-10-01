# -*- mode:python -*-
# 
# Copyright (c) Dimitry Kloper <kloper@users.sf.net> 2002-2012
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE_1_0.txt or copy at
#  http://www.boost.org/LICENSE_1_0.txt)
#
# This file is part of dgscons library (https://github.com/kloper/dgscons.git)
#
# dgscons/tools/hardlink.py -- make SCons create hard links insread of 
#                              file copies on windows
#

import sys
import SCons

def CreateHardLink(fs, src, dst):
    import ctypes
    if not ctypes.windll.kernel32.CreateHardLinkA(dst, src, 0): 
        raise OSError

def generate(env):
    if sys.platform == 'win32':
        SCons.Node.FS._hardlink_func = CreateHardLink

def exists(env):
     if sys.platform == 'win32':
         return True
     else:
         return False





