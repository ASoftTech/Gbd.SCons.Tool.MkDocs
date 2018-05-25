"""
This acts as a wrapper around the original SCons testing framework
so that we can use it from pytest as a fixture

The original TestSCons files have been updated in terms of fomatting
to bring them inline with pep8, although I suspect a re-write may be in order.

  * There's a bit too much code bundled into one class
    ideally some seperation may be in order to avoid code bloat.
  * If pytest is adopted further down the line, then we could look into
    making use of pytest's options / fixtures / tmpdir etc
  * sys.exit(1) commented out so that pytest can evaluate
  * see https://github.com/kvas-it/pytest-console-scripts/blob/master/pytest_console_scripts.py
    for an example of using options
  * There may be old code to be cleared out, if a re-write is done then it may be best to start
    fresh then add things in as they're needed.
  * This could do with being rolled into a seperate python pip package for plugins in general
"""

import pytest
from .TestSCons import TestSCons


@pytest.fixture
def scons_qmtest():
    """Provide a way for users to pull in a TestScons class via a fixture"""
    return TestSCons()
