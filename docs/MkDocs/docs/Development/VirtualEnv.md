# Python Virtual Environment Setup

## Setup

In order to setup some virtual environments for development
```
scons --setup-envs
```

This is a shortcut to
```
tox -c build/tox_dev.ini
```

There should be 3 environments setup

  * build/py36dev - development against python 3.6
  * build/py27dev - development against python 2.7
  * build/py36docs - used for generating docs using mkdocs for github pages

## Entering the environment

To enter into the environment at the command line
```
cd build
# For windows
setup_venv.bat
# For Linux
setup_venv.sh
```

The default will be py36dev,
although one of the others can be selected just by adding the name as a option
