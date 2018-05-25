"""
Common code associated with mkdocs combine utility
"""
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

# These import lines not required, but it helps intellisense within VStudio
import SCons.Script
from SCons.Environment import Environment


def detect(env):
    """Detect if mkdocscombine exe is detected on the system
       or use user specified option"""
    if 'Mkdocs_Combine' in env:
        return env.Detect(env['Mkdocs_Combine'])
    else:
        return env.Detect('mkdocscombine')


def emitter(target, source, env):
    # Choose mkdocs.yml as source file if not specified
    if not source:
        cfgfile = File('mkdocs.yml')
        source.append(cfgfile)
    else:
        cfgfile = source[0]
    # Read mkdocs config
    yamlcfg, sitedirnode, docsdirnode = Mkdocs_Readconfig(cfgfile, env)
    # Default target
    if not target:
        target = File(path.join(str(sitedirnode), 'export/mkdocs.pd'))
    return target, source
