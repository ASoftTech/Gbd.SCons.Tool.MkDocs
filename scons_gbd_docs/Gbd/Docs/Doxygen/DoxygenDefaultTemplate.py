"""
This tool will generate default template files for doxygen
"""

from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

import SCons.Script
from SCons.Environment import Environment

import os
import sys
import os.path as path
from scons_gbd_docs.Gbd.Docs.Doxygen.Common import DoxygenCommon
from scons_gbd_docs.Gbd.Docs.Doxygen.Common.DoxygenConfig import DoxygenConfig
from SCons.Script import Builder


def exists(env):
    """Check if we're okay to load this builder"""
    return DoxygenCommon.detect(env)


def generate(env):
    """Called when the tool is loaded into the environment at startup of script"""
    assert(exists(env))
    if 'Doxygen_Config' not in env:
        env['Doxygen_Config'] = DoxygenConfig(env)
    env['Doxygen_Config'].set_defaults()

    scanner = env.Scanner(
        DoxygenCommon.scanner,
        name="DoxygenScanner",
        scan_check=DoxygenCommon.scanner_check
    )
    bld = Builder(
        action=__Build_func,
        emitter=MkdocsCommon.emmiter,
        source_scanner=scanner,
        target_factory=env.fs.Entry
        single_source=True,
    )
    env.Append(BUILDERS={'DoxygenDefaultTemplate': bld})


def __Build_func(target, source, env):
    """Actual builder that does the work after the Sconscript file is parsed"""
    cfg = env['Doxygen_Config']
    assert isinstance(cfg, DoxygenConfig)

    cmdopts = [cfg.Exe]
    cmdopts += ["-w", "html"]

    # TODO targets
    cmdopts += ["theme/default/header.html",
                "theme/default/footer.html",
                "theme/default/customdoxygen.css"]

    cmdopts.append(str(source[0]))
    cmdopts = cmdopts + cfg.ExtraArgs

    print('Building Doxygen default templates:')
    env.Execute(env.Action([cmdopts], chdir=cfg.WorkingDir))
