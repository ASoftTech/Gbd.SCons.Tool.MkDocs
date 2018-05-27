"""
Configuration class for Pandoc CLI options
"""
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

import SCons.Script
from SCons.Environment import Environment


class PandocConfig:

    def __init__(self, env):
        self.env = env

    @property
    def Exe(self):
        """Represents the pandoc executable."""
        return self.env['Pandoc_Exe']

    @Exe.setter
    def Exe(self, value):
        self.env['Pandoc_Exe'] = value

    @property
    def WorkingDir(self):
        """Working directory (current directory by default)."""
        return self.env['Pandoc_WorkingDir']

    @WorkingDir.setter
    def WorkingDir(self, value):
        self.env['Pandoc_WorkingDir'] = value

    @property
    def StripEmptyParagraphs(self):
        """Represents the mkdocs combine executable."""
        return self.env['Pandoc_StripEmptyParagraphs']

    @StripEmptyParagraphs.setter
    def StripEmptyParagraphs(self, value):
        self.env['Pandoc_StripEmptyParagraphs'] = value

    @property
    def ExtraArgs(self):
        """Additional Arguments."""
        return self.env['Pandoc_ExtraArgs']

    @ExtraArgs.setter
    def ExtraArgs(self, value):
        self.env['Pandoc_ExtraArgs'] = value

    def set_defaults(self):
        """Set the default options"""
        self.env.SetDefault(
            Pandoc_Exe='pandoc',
            Pandoc_WorkingDir=self.env.Dir('.'),
            Pandoc_StripEmptyParagraphs=None,
            Pandoc_ExtraArgs=[],
        )
