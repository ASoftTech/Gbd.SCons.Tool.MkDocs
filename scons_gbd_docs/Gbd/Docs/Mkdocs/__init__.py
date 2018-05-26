"""
If the user requests "Gbd.Docs.Mkdocs" then this will call this script as a tool
In which case we include all the builders
"""
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

from . import MkdocsServer, MkdocsBuild
from . import MkdocsPublish, MkdocsCombiner


def generate(env):
    MkdocsBuild.generate(env)
    MkdocsCombiner.generate(env)
    MkdocsPublish.generate(env)
    MkdocsServer.generate(env)


def exists(env):
    if not MkdocsBuild.exists(env):
        return False
    if not MkdocsCombiner.exists(env):
        return False
    if not MkdocsPublish.exists(env):
        return False
    if not MkdocsServer.exists(env):
        return False
    return True
