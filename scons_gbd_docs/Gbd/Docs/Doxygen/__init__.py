"""
    __init__.py
    If the user requests "Gbd.Docs.Doxygen"
    then this will call this script as a tool
    In which case we include all the builders
"""

from . import Doxygen, DoxygenDefaultTemplate


def generate(env):
    Doxygen.generate(env)
    DoxygenDefaultTemplate.generate(env)


def exists(env):
    if not Doxygen.exists(env):
        return False
    if not DoxygenDefaultTemplate.exists(env):
        return False
    return True
