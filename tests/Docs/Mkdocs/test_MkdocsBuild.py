"""
Run tests for the MkdocsBuild tool
"""

from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

import pytest
import py
import os


def get_absdir(src):
    """Find the absolute path of the dir relative to this module"""
    curdir = os.path.dirname(__file__)
    imgdir = os.path.join(curdir, src)
    return imgdir


def test_basic(scons_qmtest):

    # TODO path not being detected correctly
    scons_qmtest.program = 'scons'
    scons_qmtest.dir_fixture(get_absdir('image'))
    scons_qmtest.run(arguments='.')

    x1 = scons_qmtest._stderr
    assert x1[0] == ''
    x2 = 5

    # New way using pytest-console-scripts
    #ret = script_runner.run('scripts/py36dev/Scripts/scons.py', '--version')
    #assert ret.success
    # just for example, let's assume that foobar --version
    # should output 3.2.1
    #assert ret.stdout == '3.2.1\n'
    #assert ret.stderr == ''

    # Old way
    #test = TestSCons.TestSCons(program='scripts/py36dev/Scripts/scons.py')
    #test.dir_fixture(get_imagedir('image'))

    #test.run(arguments='. build', stdout="""\
#scons: Reading SConscript files ...
#test123
    #""")
    #test.pass_test()

    #setup_imagedir('image', tmpdir)

    #x1 = __name__

    #with capsys.disabled():
    #    print('TODO')
    #    print(imagedir.dirpath())
    #assert 5 == 5

#def setup_imagedir(src, dest):
#    moddir = py.path.local(os.path.dirname(__file__))
#    srcdir = moddir.join(src)
#    srcdir.copy(dest)

#def test_create_file(tmpdir):
#    p = tmpdir.mkdir("sub").join("hello.txt")
#    p.write("content")
#    assert p.read() == "content"
#    assert len(tmpdir.listdir()) == 1
#    print(tmpdir.dirpath)
#    assert 0
