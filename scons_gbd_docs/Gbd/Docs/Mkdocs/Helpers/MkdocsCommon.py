"""
Common code associated with mkdocs builders
"""
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

# These import lines not required, but it helps intellisense within VStudio
import SCons.Script
from SCons.Environment import Environment

import os
import sys
import os.path as path
from SCons.Script import File, Dir
from scons_gbd_docs.Gbd.Docs.Mkdocs.Helpers.MkdocsConfig import MkdocsConfig


def detect(env):
    """Detect if mkdocs exe is detected on the system
       or use user specified option"""
    if 'Mkdocs' in env:
        ret = env.Detect(env['Mkdocs'])
    else:
        ret = env.Detect('mkdocs')
    if ret is None:
        print("mkdocs not found")
    return ret


def scanner(node, env, path, arg=None):
    """Dependency scanner for listing all files within the mkdocs source
    directory (typically docs). We exclude the doxygen dir since it
    has quite a lot of content and requires a clean build anyway
    Args:
        node: the SCons directory node to scan
        env:  the current SCons environment
        path: not used
        arg:  not used
    Returns:
        A list of files.
    """
    # Read mkdocs config
    cfg = env['Mkdocs_Config']
    assert isinstance(cfg, MkdocsConfig)

    # Look at the docs source directory
    searchpath = env.subst(cfg.DocsDir.abspath)

    # Search patterns to exclude
    excludedirs_full = []

    for excludeitem in env['Mkdocs_ExcludeDirs']:
        excludedirs_full.append(os.path.join(searchpath, excludeitem))

    depends = []
    for d, unused_s, files in os.walk(searchpath, topdown=True):
        for excludeitem in excludedirs_full:
            if d.startswith(excludeitem):
                continue
        for f in files:
            depends.append(File(os.path.join(d, f)))
    return depends


def emitter(target, source, env):
    # Choose mkdocs.yml as source file if not specified
    if not source:
        cfgfile = File('mkdocs.yml')
        source.append(cfgfile)
    else:
        cfgfile = source[0]
    # Read mkdocs config

    cfg = env['Mkdocs_Config']
    assert isinstance(cfg, MkdocsConfig)
    cfg.read_cfg(cfgfile)

    # We need at least one target that's a file for the rebuild
    # for source changes logic to work in scons
    filenode = File(path.join(str(cfg.SiteDir), 'mkdocs/search_index.json'))
    target.append(filenode)
    env.Clean(target, cfg.SiteDir)
    return target, source
