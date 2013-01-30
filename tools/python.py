# -*- mode:python -*-
# 
# Copyright (c) Dimitry Kloper <kloper@users.sf.net> 2002-2012
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE_1_0.txt or copy at
#  http://www.boost.org/LICENSE_1_0.txt)
# 
# This file is part of dgscons library (https://github.com/kloper/dgscons.git)
#
# dgscons/tools/python.py -- python configuration Tool for SCons 
#

import os
import sys
import string

from dgscons import DGSConsException
from SCons.Script import ARGUMENTS

def find():
    python_include = ARGUMENTS.get('pythoninc')
    python_lib = ARGUMENTS.get('pythonlib')
    return (python_include, python_lib)

def generate(env):
    (python_include, python_lib) = find()
    if not python_include:
        raise DGSConsException("pythoninc not defined")
    if not python_lib:
        raise DGSConsException("pythonlib not defined")
    env['PYTHONLIBDIR'] = python_lib
    env['PYTHONINCDIR'] = python_include

def exists(env):
    (python_include, python_lib) = find()
    if not python_include:
        return False
    if not python_lib:
        return False
    return True




