# Python Virtual Environment Setup


## Virtual Environment

An example to setup a python virtual environment

For Windows:
```
setup_py36dev.bat
```
For Linux:
```
setup_py36dev.sh
```

This will create a python virtual environment within the py36dev directory.
Any tools required will be installed at this point via pip / the reading in of **requirements_py3.txt**

To create a new requirements_py3.txt after instaling some additional tools
```
pip freeze > requirements_py3.txt
```

