"""
    PandocBuild
    This tool will generate the documentation output from input files
    For example converting markdown files to a pdf
"""

import SCons.Script
from SCons.Environment import Environment

from SCons.Script import *
import os
import sys
import os.path as path
from . import PandocCommon

# TODO Add options / settings


def exists(env):
    """Check if we're okay to load this builder"""
    return PandocCommon.detect(env)


def generate(env):
    """Called when the tool is loaded into the environment
       at startup of script"""
    assert(exists(env))
    # Available Options
    # These override those within the yaml configuration file
    env.SetDefault(
        # Working directory is current directory (default)
        Pandoc_WorkingDir=env.Dir('.'),

        # TODO additional options

        # Additional Arguments
        Pandoc_ExtraArgs=[])

    # Register the builder
    bld = Builder(action=__PandocBuild_func)
    env.Append(BUILDERS={'PandocBuild': bld})


def __PandocBuild_func(target, source, env):
    """Actual builder that does the work after the Sconscript file is parsed"""
    cmdopts = [_detect(env)]

    index = 0
    for srcitem in source:
        infile = str(srcitem)
        outfile = str(target[index])

        # TODO add options
        cmdopts = cmdopts + env['Pandoc_ExtraArgs']

        cmdopts.append('--output=' + outfile)
        cmdopts.append(infile)

        print('Building Pandoc Documentation:')
        env.Execute(env.Action([cmdopts], chdir=env['Pandoc_WorkingDir']))
