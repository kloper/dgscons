# -*- mode:python -*-
# 
# Copyright (c) Dimitry Kloper <kloper@users.sf.net> 2002-2012
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE_1_0.txt or copy at
#  http://www.boost.org/LICENSE_1_0.txt)
# 
# This file is part of dgscons library (https://github.com/kloper/dgscons.git)
#
# dgscons/tools/glib.py -- glib configuration Tool for SCons 
#

import os
import sys
import string

from dgscons import DGSConsException
from SCons.Script import ARGUMENTS

def find():
    glib_include = ARGUMENTS.get('glibinc')
    glib_lib = ARGUMENTS.get('gliblib')
    glib_bin = ARGUMENTS.get('glibbin')
    return (glib_include, glib_lib, glib_bin)

def generate(env):
    (glib_include, glib_lib, glib_bin) = find()
    if not glib_include:
        raise DGSConsException("glibinc not defined")
    if not glib_lib:
        raise DGSConsException("gliblib not defined")
    if not glib_bin:
        raise DGSConsException("glibbin not defined")
    env['GLIBLIBDIR'] = glib_lib
    env['GLIBINCDIR'] = glib_include
    env['GLIBBINDIR'] = glib_bin
    env['GLIB_GENMARSHAL'] = os.path.join( glib_bin, 'glib-genmarshal.exe')


def exists(env):
    (glib_include, glib_lib, bin) = find()
    if not glib_include:
        return False
    if not glib_lib:
        return False
    if not glib_bin:
        return False
    return True




