"""
This tool will generate the documentation output as json
using markdown files as an input via mkdocs to an output directory
"""
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

# These import lines not required, but it helps intellisense within VStudio
import SCons.Script
from SCons.Environment import Environment

import os
import sys
import os.path as path
from .Helpers import MkdocsCommon
from .Helpers.MkdocsConfig import MkdocsConfig
from SCons.Script import Builder


def exists(env):
    """Check if we're okay to load this builder"""
    return MkdocsCommon.detect(env)


def generate(env):
    """Called when the tool is loaded into the environment at startup of script"""
    assert(exists(env))
    if 'Mkdocs_Config' not in env:
        env['Mkdocs_Config'] = MkdocsConfig(env)

    scanner = env.Scanner(
        MkdocsCommon.scanner,
        name='MkdocsScanner'
    )
    bld = Builder(
        action=__Build_func,
        emitter=MkdocsCommon.emitter,
        source_scanner=scanner,
    )
    env.Append(BUILDERS={'MkdocsJsonBuild': bld})


def __Build_func(target, source, env):
    """Actual builder that does the work after the SConstruct file is parsed"""
    cmdopts = ['$Mkdocs', 'json']
    cmdopts.append('--config-file=' + str(source[0]))

    cfg = env['Mkdocs_Config']
    assert isinstance(cfg, MkdocsConfig)

    if cfg.CleanBuild:
        cmdopts.append('--clean')
    elif not cfg.CleanBuild:
        cmdopts.append('--dirty')
    if cfg.Strict:
        cmdopts.append('--strict')
    if cfg.SiteDir:
        cmdopts.append('--site-dir=$Mkdocs_SiteDir')
    if cfg.Quiet:
        cmdopts.append('--quiet')
    if cfg.Verbose:
        cmdopts.append('--verbose')
    cmdopts = cmdopts + cfg.ExtraArgs

    print('Building MkDocs Documentation as Json:')
    env.Execute(env.Action([cmdopts], chdir=cfg.WorkingDir))
