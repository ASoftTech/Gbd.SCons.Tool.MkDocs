"""
This tool will publish the mkdocs content to a github pages destination
"""
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

import SCons.Script
from SCons.Environment import Environment

import os
import sys
import os.path as path
from scons_gbd_docs.Gbd.Docs.Mkdocs.Common import MkdocsCommon
from scons_gbd_docs.Gbd.Docs.Mkdocs.Common.MkdocsConfig import MkdocsConfig
from SCons.Script import Builder

# If you ever want to remove the remote published branch you can use
# git push origin --delete gh-pages


def exists(env):
    """Check if we're okay to load this builder"""
    return MkdocsCommon.detect(env)


def generate(env):
    """Called when the tool is loaded into the environment at startup of script"""
    assert(exists(env))
    if 'Mkdocs_Config' not in env:
        env['Mkdocs_Config'] = MkdocsConfig(env)
    env['Mkdocs_Config'].set_defaults()

    scanner = env.Scanner(
        MkdocsCommon.scanner,
        name='MkdocsScanner'
    )
    bld = Builder(
        action=__Publish_func,
        emitter=MkdocsCommon.emitter,
        source_scanner=scanner,
    )
    env.Append(BUILDERS={'__MkdocsPublish': bld})
    env.AddMethod(MkdocsPublish, 'MkdocsPublish')


def MkdocsPublish(env, commitmsg, target=None, source=None):
    """Wrapper for the Builder
       so that we can use a default on the source parameter"""
    return env.__MkdocsPublish(target, source, Mkdocs_CommitMsg=commitmsg)


def __Publish_func(target, source, env):
    """Actual builder that does the work after the SConstruct file is parsed"""
    cfg = env['Mkdocs_Config']
    assert isinstance(cfg, MkdocsConfig)

    cmdopts = [cfg.Exe, 'gh-deploy']
    cmdopts.append('--config-file=' + str(source[0]))

    if cfg.CleanBuild:
        cmdopts.append('--clean')
    elif not cfg.CleanBuild:
        cmdopts.append('--dirty')
    if not env['Mkdocs_CommitMsg']:
        raise Exception('No commit message specified')
    cmdopts.append('--message="$Mkdocs_CommitMsg"')
    if cfg.RemoteBranch:
        cmdopts.append('--remote-branch=$Mkdocs_RemoteBranch')
    if cfg.RemoteName:
        cmdopts.append('--remote-name=$Mkdocs_RemoteName')
    if cfg.ForcePush:
        cmdopts.append('--force')
    if cfg.Quiet:
        cmdopts.append('--quiet')
    if cfg.Verbose:
        cmdopts.append('--verbose')
    cmdopts = cmdopts + cfg.ExtraArgs

    print('Pushing MkDocs Documentation to github pages:')
    env.Execute(env.Action([cmdopts], chdir=cfg.WorkingDir))
