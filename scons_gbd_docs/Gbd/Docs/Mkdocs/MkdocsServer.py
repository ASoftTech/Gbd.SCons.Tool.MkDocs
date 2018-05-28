"""
This tool can be used to serve / preview the mkdocs
output locally before publishing
"""
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

import SCons.Script
from SCons.Environment import Environment

import os
import sys
import os.path as path
from scons_gbd_docs.Gbd.Docs.Mkdocs.Common import MkdocsCommon
from scons_gbd_docs.Gbd.Docs.Mkdocs.Common.MkdocsConfig import MkdocsConfig
from SCons.Script import Builder


def exists(env):
    """Check if we're okay to load this builder"""
    return MkdocsCommon.detect(env)


def generate(env):
    """Called when the tool is loaded into the environment at startup of script"""
    assert(exists(env))
    if 'Mkdocs_Config' not in env:
        env['Mkdocs_Config'] = MkdocsConfig(env)
    env['Mkdocs_Config'].set_defaults()

    scanner = env.Scanner(
        MkdocsCommon.scanner,
        name='MkdocsScanner'
    )
    bld = Builder(
        action=__Server_func,
        emitter=MkdocsCommon.emitter,
        source_scanner=scanner,
    )
    env.Append(BUILDERS={'MkdocsServer': bld})


def __Server_func(target, source, env):
    """Actual builder that does the work after the SConstruct file is parsed"""
    cfg = env['Mkdocs_Config']
    assert isinstance(cfg, MkdocsConfig)

    cmdopts = [cfg.Exe, 'serve']
    cmdopts.append('--config-file=' + str(source[0]))

    serverurl = '127.0.0.1:8000'
    if cfg.ServeUrl:
        serverurl = str(cfg.ServeUrl)
        cmdopts.append('--dev-addr=$Mkdocs_ServeUrl')
    if cfg.Strict:
        cmdopts.append('--strict')
    if cfg.Theme:
        cmdopts.append('--theme=$Mkdocs_Theme')
    if cfg.CustomDir:
        cmdopts.append('--theme-dir=$Mkdocs_CustomDir')
    if cfg.LiveReload:
        cmdopts.append('--livereload')
    elif not cfg.LiveReload:
        cmdopts.append('--no-livereload')
    if cfg.DirtyReload:
        cmdopts.append('--dirtyreload')
    if cfg.Quiet:
        cmdopts.append('--quiet')
    if cfg.Verbose:
        cmdopts.append('--verbose')
    cmdopts = cmdopts + cfg.ExtraArgs

    print('Starting MkDocs Server http://' + serverurl)
    env.Execute(env.Action([cmdopts], chdir=cfg.WorkingDir))
    print('Server Closed.')
