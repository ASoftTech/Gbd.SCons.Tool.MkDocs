"""
    PandocCommon
    Common code associated with pandoc builders
"""

# These import lines not required, but it helps intellisense within VStudio
import SCons.Script
from SCons.Environment import Environment

from SCons.Script import File, Dir
import os
import sys
import os.path as path
import yaml


def detect(env):
    """Detect if mkdocs exe is detected on the system
       or use user specified option"""
    if 'Mkdocs' in env:
        return env.Detect(env['Mkdocs'])
    else:
        return env.Detect('mkdocs')
