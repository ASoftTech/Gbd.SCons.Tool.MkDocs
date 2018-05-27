# Scons Development

## Installing repo source into virtual env

To install the source for this repo into the virtual env
first enter the virtual env

```
cd build
# For windows
setup_venv.bat
# For Linux
setup_venv.sh
```

Next to install the repo into the virtual env
```
pip install git+https://github.com/ASoftTech/Scons.Gbd.Docs
```

To uninstall
```
pip uninstall scons-gbd-docs
```


## Switching to development scons

First enter the virtual env, then uninstall the stable scons that's installed by default
```
pip uninstall scons
```

Next download the source for scons (make sure to do this in the build directory)
```
cd build
git clone https://github.com/SCons/scons.git
cd scons
```

To checkout specific version
```
git checkout rel_3.0.1
```

Next to build scons use one of the following commands

  * `c:\Python36\Scripts\scons.py build/scons`
  * `bootstrap.py build/scons`
  * `scons build/scons`

I've noticed that trying to build scons within a virtual env results in errors
so you may need to leave the virtual env with `deactivate` while building

Next to install scons via pip into the virtual env
Make sure to enter into the virtual env, and that your inside the build/scons directory
then run the following
```
pip install build\scons
```
