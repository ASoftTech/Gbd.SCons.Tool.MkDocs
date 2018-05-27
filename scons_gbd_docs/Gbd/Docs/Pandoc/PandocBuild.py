"""
This tool will generate the documentation output using pandoc in varying formats
For example converting markdown files to a pdf
"""
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

import SCons.Script
from SCons.Environment import Environment

import os
import sys
import os.path as path
from scons_gbd_docs.Gbd.Docs.Pandoc.Common import PandocCommon
from scons_gbd_docs.Gbd.Docs.Pandoc.Common.PandocConfig import PandocConfig
from SCons.Script import Builder


def exists(env):
    """Check if we're okay to load this builder"""
    return PandocCommon.detect(env)


def generate(env):
    """Called when the tool is loaded into the environment at startup of script"""
    assert(exists(env))
    if 'Pandoc_Config' not in env:
        env['Pandoc_Config'] = PandocConfig(env)
    env['Pandoc_Config'].set_defaults()

    bld = Builder(
        action=__Build_func,
    )
    env.Append(BUILDERS={'PandocBuild': bld})


def __Build_func(target, source, env):
    """Actual builder that does the work after the SConstruct file is parsed"""
    cfg = env['Pandoc_Config']
    assert isinstance(cfg, PandocConfig)

    cmdopts = [cfg.Exe, 'build']

    if cfg.StripEmptyParagraphs:
        cmdopts.append('--strip-empty-paragraphs')

    # TODO options
    #cmdopts.append('--config-file=' + str(source[0]))
    #if cfg.CleanBuild:
    #    cmdopts.append('--clean')
    #elif not cfg.CleanBuild:
    #    cmdopts.append('--dirty')
    #if cfg.Strict:
    #    cmdopts.append('--strict')
    #if cfg.Theme:
    #    cmdopts.append('--theme=$Mkdocs_Theme')
    #if cfg.ThemeDir:
    #    cmdopts.append('--theme-dir=$Mkdocs_ThemeDir')
    #if 'Mkdocs_SiteDir' in env:
    #    cmdopts.append('--site-dir=$Mkdocs_SiteDir')
    #if cfg.Quiet:
    #    cmdopts.append('--quiet')
    #if cfg.Verbose:
    #    cmdopts.append('--verbose')
    cmdopts = cmdopts + cfg.ExtraArgs

    print('Building Pandoc Documentation:')

    index = 0
    for srcitem in source:
        infile = str(srcitem)
        outfile = str(target[index])
        index = index + 1

        runopts = cmdopts
        runopts.append('--output=' + outfile)
        runopts.append(infile)
        env.Execute(env.Action([runopts], chdir=cfg.WorkingDir))
