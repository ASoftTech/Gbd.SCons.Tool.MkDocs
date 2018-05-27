# Testing

## Running Tests

In order to run the tests we can use
```
scons --run-tests
```

This is just a shortcut to calling `setup.py test`
Which in turn uses `pytest` with a set of options within setup.cfg

The .vscode directory also contains the needed setup to debug the tests and examples via Visual Studio Code


## Test Configuration

### Setup.cfg

First we have a section within **setup.cfg**
This just tells setup.py to use pytest by default when running tests
```
[aliases]
test=pytest
```

Next we have the following within **setup.cfg**
```
[tool:pytest]
addopts=--codestyle -v --cov scons_gbd_docs --ignore=scripts --ignore=tests/pytest_scons/framework
codestyle_ignore = E501 E265
cache_dir = .vscode/temp/.pytest_cache
python_paths = scripts/py36dev/Lib/site-packages/scons-3.0.1 scripts/py36dev/Scripts
```

This just provides some options to pytest for testing / ignoring features.

  * addopts - uses --codestyle to use the pytest-codestyle plugin for checking the language
    to see if it follows pep8 standards
  * we ignore tests/pytest_scons/framework for the tests since it's existing scons code
  * codestyle_ignore - specifies which errors to ignore from codestyle
  * cache_dir - specify a different temporary directory for the pytest cache
  * python_paths - we add scons to the pythonpath to help finding scons when debugging

### conftest.py

Within the tests directory we have a conftest.py file

  * https://docs.pytest.org/en/latest/plugins.html

```
pytest_plugins = "tests.pytest_scons.framework.scons_qmtest"
```

This line of code tells pytest to load the module tests.pytest_scons.framework.scons_qmtest as a pytest plugin


## Coverage

As part of the virtual environment pytest-cov is installed which uses the coverage command.
This determines what percentage of the code is being tested by the tests so far.
So it's a good indicator as to if more tests are needed to cover more of the existing code in the library
