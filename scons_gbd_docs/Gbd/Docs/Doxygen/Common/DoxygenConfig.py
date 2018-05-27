"""
Configuration class for Doxygen CLI options
"""
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

import SCons.Script
from SCons.Environment import Environment


class DoxygenConfig:

    def __init__(self, env):
        self.env = env

    @property
    def Exe(self):
        """Represents the doxygen executable."""
        return self.env['Doxygen_Exe']

    @Exe.setter
    def Exe(self, value):
        self.env['Doxygen_Exe'] = value

    @property
    def WorkingDir(self):
        """Working directory (current directory by default)."""
        return self.env['Doxygen_WorkingDir']

    @WorkingDir.setter
    def WorkingDir(self, value):
        self.env['Doxygen_WorkingDir'] = value

    @property
    def ExtraArgs(self):
        """Additional Arguments."""
        return self.env['Doxygen_ExtraArgs']

    @ExtraArgs.setter
    def ExtraArgs(self, value):
        self.env['Doxygen_ExtraArgs'] = value

    def set_defaults(self):
        """Set the default options"""
        self.env.SetDefault(
            Doxygen_Exe='doxygen',
            Doxygen_WorkingDir=self.env.Dir('.'),
            Doxygen_ExtraArgs=[],
        )
