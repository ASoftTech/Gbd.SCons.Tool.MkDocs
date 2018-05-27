# TODO

## Development

  * document switch to developer scons scons-3.1.0.alpha.yyyymmdd in virtual env
  * look at https://bitbucket.org/scons/scons/wiki/ToolsIndex
  * look at https://bitbucket.org/scons/scons/wiki/ContributedBuilders
  * example scripts https://github.com/raimon49/mkdocs-safe-text-plugin
  * write some code for scons to make use of entry points for pulling in tools

## Testing

  * setup all tests / check coverage
  * Test cleanup in all instances
  * setup tox-tests for testing against all virtual envs (see mkdocs)

## Linux

  * test scripts under linux

## Builders

### MkdocsCombiner

  * Account for arrays / lists in the exclusion list

  * tornado 4.5.3 or 5.0.1 for python3.6? / mkdocs
  * double check python 3.5 vs python 3.6 installed packages

## Look at later on

  * switch between py virtual envs in vscode settings?
  * is there a way to list tasks in a treeview in vscode?
  * remove SConstruct files once scons is released that supports SConstruct.py
