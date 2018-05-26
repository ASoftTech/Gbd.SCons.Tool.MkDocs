"""
This tool uses mkdocscombiner to generate a pd file
which can then be used with pandoc to generate a pdf or other forms of documentation
"""
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

import SCons.Script
from SCons.Environment import Environment

import os
import sys
import os.path as path
from scons_gbd_docs.Gbd.Docs.Mkdocs.Common import MkdocsCommon
from scons_gbd_docs.Gbd.Docs.Mkdocs.Common import MkdocsCombineCommon
from scons_gbd_docs.Gbd.Docs.Mkdocs.Common.MkdocsCombineConfig import MkdocsCombineConfig
from SCons.Script import Builder


def exists(env):
    """Check if we're okay to load this builder"""
    return MkdocsCombineCommon.detect(env)


def generate(env):
    """Called when the tool is loaded into the environment at startup of script"""
    assert(exists(env))
    if 'Mkdocs_CombineConfig' not in env:
        env['Mkdocs_CombineConfig'] = MkdocsCombineConfig(env)
    env['Mkdocs_CombineConfig'].set_defaults()

    scanner = env.Scanner(
        MkdocsCommon.scanner,
        name='MkdocsScanner'
    )
    bld = Builder(
        action=__Combiner_func,
        emitter=MkdocsCombineCommon.emitter,
        source_scanner=scanner,
    )
    env.Append(BUILDERS={'MkdocsCombiner': bld})


def __Combiner_func(target, source, env):
    """Actual builder that does the work after the SConstruct file is parsed"""
    cmdopts = ['$Mkdocs_Combine_Exe']
    cmdopts.append('--config-file=' + str(source[0]))

    cfg = env['Mkdocs_CombineConfig']
    assert isinstance(cfg, MkdocsCombineConfig)

    if cfg.OutputHtml:
        cmdopts.append('--outhtml=' + str(target[0]))
    else:
        cmdopts.append('--outfile=' + str(target[0]))

    # File options
    if cfg.Encoding:
        cmdopts.append('--encoding=$Mkdocs_Combine_Encoding')
    # TODO parse list as input
    if cfg.Exclude:
        cmdopts.append('--exclude=$Mkdocs_Combine_Exclude')

    # Structure options
    if cfg.Meta:
        cmdopts.append('--meta')
    elif not cfg.Meta:
        cmdopts.append('--no-meta')
    if cfg.Titles:
        cmdopts.append('--titles')
    elif not cfg.Titles:
        cmdopts.append('--no-titles')
    if cfg.Uplevels:
        cmdopts.append('--up-levels')
    elif not cfg.Uplevels:
        cmdopts.append('--keep-levels')

    # Table options
    if cfg.PandocTables:
        cmdopts.append('--grid-tables')
    elif not cfg.PandocTables:
        cmdopts.append('--tables')
    if cfg.TableWidth:
        cmdopts.append('--grid-width=$Mkdocs_Combine_TableWidth')

    # Link options
    if cfg.Refs:
        cmdopts.append('--refs')
    elif not cfg.Refs:
        cmdopts.append('--no-refs')
    if cfg.Anchors:
        cmdopts.append('--anchors')
    elif not cfg.Anchors:
        cmdopts.append('--no-anchors')

    # Extra options
    if cfg.MathLatex:
        cmdopts.append('--latex')
    elif not cfg.MathLatex:
        cmdopts.append('--math')
    if cfg.ImageExt:
        cmdopts.append('--image-ext=$Mkdocs_Combine_ImageExt')
    cmdopts = cmdopts + cfg.ExtraArgs

    print('Building MkDocs Documentation as combined markdown file:')
    env.Execute(env.Action([cmdopts], chdir=cfg.WorkingDir))
