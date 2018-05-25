"""
    __init__.py
    If the user requests "Gbd.Docs.Pandoc"
    then this will call this script as a tool
    In which case we include all the builders
"""

from . import PandocBuild


def generate(env):
    PandocBuild.generate(env)


def exists(env):
    if not PandocBuild.exists(env):
        return False
    return True
