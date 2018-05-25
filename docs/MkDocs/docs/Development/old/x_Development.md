# Development


## Plugin


### Installing Development Sources

To install the development sources.
First enter the virtual env if there is one

To install
```
pip install git+https://github.com/ASoftTech/Scons.Gbd.Docs.git
```

To uninstall
```
pip uninstall scons-gbd-tools-docs
```


## SCons


### Using stable scons

In order to test against stable scons, within the python virtual environment
```
pip install scons
```


### Using development scons

In order to test against development scons
```
cd scripts
git clone https://github.com/SCons/scons.git
cd scons
```

To checkout specific version
```
git checkout rel_3.0.1
```

To build scons use one of the following
```
c:\Python36\Scripts\scons.py build/scons
bootstrap.py build/scons
scons build/scons
```
I've noticed that trying to build scons within a virtual env results in errors

Next to install scons via pip into the virtual env
I've noticed the --egg option works when doing this without any modifications
I recommend just adding this patch in if using scons devel to avoid that
https://bitbucket.org/bdbaddog/scons/commits/c89c850e906fa0e2cc2bd70c5bf4dabfe4241e8d?at=default

Then we can use
```
cd ..
setup_py36dev.bat
pip install scons\build\scons
```
