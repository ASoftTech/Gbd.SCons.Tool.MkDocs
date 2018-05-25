# Setup


## setup.py / setup.cfg

  * setup.py - python script used during installation / to add metadata for pip
  * setup.cfg - general configuration for setup.py

This just sets a temporary directory to be within .vscode so it doesn't show up in root
```
[egg_info]
egg_base = .vscode/temp
```
