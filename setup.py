"""Setup file to package scons mkdocs tools"""

import os
from setuptools import setup, find_packages

from scons_gbd_docs import (__version__ as VERSION, __author__ as AUTHOR,
                                  __license__ as LICENSE)


def read_file(filename):
    basepath = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(basepath, filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''


LONG_DESC = ''
try:
    from pypandoc import convert
    readme = convert('Readme.md', 'rst', format='markdown_github')
    change_log = convert('Changelog.md', 'rst', format='markdown_github')
    LONG_DESC = readme + '\n\n' + change_log
except (IOError, ImportError):
    LONG_DESC = read_file('Readme.md')


#from codecs import open  # To use a consistent encoding
#from os import path

# Get the long description from the relevant file
#here = path.abspath(path.dirname(__file__))
#with open(path.join(here, 'README.md'), encoding='utf-8') as f:
#    long_description = f.read()

#def get_packages(package):
#    """Return root package and all sub-packages."""
#    return [dirpath
#            for dirpath, dirnames, filenames in os.walk(package)
#            if os.path.exists(os.path.join(dirpath, '__init__.py'))]
#     packages=get_packages("scons_gbd_docs"),


setup(
    name='scons-gbd-tools-docs',
    version=VERSION,
    description='SCons tools for generating documentation.',
    long_description=LONG_DESC,
    author=AUTHOR,
    author_email='garlicbready@googlemail.com',
    url='http://ASoftTech.github.io/Scons.Gbd.Docs',
    classifiers=[
        #   3 - Alpha, 4 - Beta, 5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Documentation',
        'Topic :: Text Processing',
    ],
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    zip_safe=False,
    keywords="pip package, mkdocs, scons, pandoc",
    license=LICENSE,
    install_requires=[
        "mkdocs>=0.16.3",
        "mkdocs-pandoc>=0.2.6",
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest-cov',
        'pytest-pycodestyle',
        'pytest-runner',
        'pytest-colordots',
    ],
    entry_points={
        'scons.plugins': [
            'scons_gbd_docs=scons_gbd_docs.plugin:GbdDocTools',
        ]
    }
)
