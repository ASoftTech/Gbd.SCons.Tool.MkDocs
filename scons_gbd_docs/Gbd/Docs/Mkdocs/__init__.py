"""
If the user requests "Gbd.Docs.Mkdocs" then this will call this script as a tool
In which case we include all the builders
"""
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

from . import MkdocsServer, MkdocsBuild, MkdocsJsonBuild
from . import MkdocsPublish, MkdocsCombiner


def generate(env):
    MkdocsServer.generate(env)
    MkdocsBuild.generate(env)
    MkdocsPublish.generate(env)
    MkdocsJsonBuild.generate(env)
    MkdocsCombiner.generate(env)


def exists(env):
    if not MkdocsServer.exists(env):
        return False
    if not MkdocsBuild.exists(env):
        return False
    if not MkdocsPublish.exists(env):
        return False
    if not MkdocsJsonBuild.exists(env):
        return False
    if not MkdocsCombiner.exists(env):
        return False
    return True
