# vim: set et sw=3 tw=0 fo=awqorc ft=python:
# -*- mode:python; coding:utf-8; -*-
#
# Astxx, the Asterisk C++ API and Utility Library.
# Copyright © 2005, 2006  Matthew A. Nicholson
# Copyright © 2006  Tim Blechmann
#
#  Copyright © 2007 Christoph Boehme
#
#  Copyright © 2012 Dirk Baechle
#
#  Copyright © 2013 Russel Winder
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License version 2.1 as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

# The original version was tested with doxygen 1.4.6

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
    )
    env.Append(BUILDERS={'DoxygenBuild': bld})


def __Build_func(target, source, env):
    """Actual builder that does the work after the Sconscript file is parsed"""
    cfg = env['Doxygen_Config']
    assert isinstance(cfg, DoxygenConfig)

    cmdopts = [cfg.Exe]
    cmdopts.append(str(source[0]))
    cmdopts = cmdopts + cfg.ExtraArgs

    print('Building Doxygen:')
    env.Execute(env.Action([cmdopts], chdir=cfg.WorkingDir))
