"""
Common code associated with mkdocs combine utility
"""
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

import SCons.Script
from SCons.Environment import Environment

import os.path as path
from SCons.Script import File, Dir
from scons_gbd_docs.Gbd.Docs.Mkdocs.Common.MkdocsConfig import MkdocsConfig


def detect(env):
    """Detect if mkdocscombine exe is detected on the system
       or use user specified option"""
    if 'Mkdocs_Combine_Exe' in env:
        ret = env.Detect(env['Mkdocs_Combine_Exe'])
    else:
        ret = env.Detect('mkdocscombine')
    if ret is None:
        print("mkdocscombine not found")
    return ret


def emitter(target, source, env):
    # Choose mkdocs.yml as source file if not specified
    if not source:
        cfgfile = File('mkdocs.yml')
        source.append(cfgfile)
    else:
        cfgfile = source[0]

    # Read mkdocs yaml file
    mkcfg = env['Mkdocs_Config']
    assert isinstance(mkcfg, MkdocsConfig)
    mkcfg.read_cfg(cfgfile)

    # Default target
    filenode = File(path.join(str(mkcfg.SiteDir), 'export/mkdocs.pd'))
    target.append(filenode)
    return target, source
