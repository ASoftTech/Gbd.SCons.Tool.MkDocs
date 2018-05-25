# Todo

Example scripts

  * https://github.com/raimon49/mkdocs-safe-text-plugin


## General

  * write more tests
  * Test cleanup in all instances
  * switch to pip installed version of scons in scripts
  * Update python2 requirements file

    SCONS_LIB_DIR=scons\build\scons\engine

  * look at https://bitbucket.org/scons/scons/wiki/ToolsIndex
  * look at https://bitbucket.org/scons/scons/wiki/ContributedBuilders

  * Once scons moves to github file a new issue
    a tool requires an exists function, it's searched for but never actually called.
    so we end up having to call it from within the generate function.
    Based on some of the mails from a couple of years ago there's plans to change the tool mechansim.
  * Take another look at relative imports within the tool loader


## Plugin Entry Points

setup scons to use entry points

  * https://stackoverflow.com/questions/774824/explain-python-entry-points
  * http://amir.rachum.com/blog/2017/07/28/python-entry-points/


## Tox

  * use tox to manage virtual envs
  * https://github.com/pytest-dev/pytest

original dirs

enginedir:
scripts\scons\build\scons\engine

bindir:
scripts\scons\build\scons\script


enginedir:
scripts\py36dev\Lib\site-packages\scons-3.1.0.alpha.yyyymmdd\

bindir:
scripts\py36dev\Scripts

scripts/py36dev/Scripts



## Builders

### MkdocsPandoc

Set this up for generating pandoc files


### MkdocsCombiner

  * Account for arrays / lists in the exclusion list

  * tornado 4.5.3 or 5.0.1 for python3.6? / mkdocs
  * double check python 3.5 vs python 3.6 installed packages

