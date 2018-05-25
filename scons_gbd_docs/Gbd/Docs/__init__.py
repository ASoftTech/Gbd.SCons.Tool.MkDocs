"""
If the user requests "Gbd.Docs" then this will call this script as a tool
In which case we include all the builders
"""
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

from . import Mkdocs
from . import Doxygen
from . import Pandoc


def generate(env):
    Mkdocs.generate(env)
    Doxygen.generate(env)
    Pandoc.generate(env)


def exists(env):
    if not Mkdocs.exists(env):
        return False
    if not Doxygen.exists(env):
        return False
    if not Pandoc.exists(env):
        return False
    return True
