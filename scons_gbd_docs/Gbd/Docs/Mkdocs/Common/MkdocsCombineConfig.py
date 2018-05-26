"""
Configuration class for Mkdocs Combiner
"""
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

import SCons.Script
from SCons.Environment import Environment


class MkdocsCombineConfig:

    def __init__(self, env):
        self.env = env

    # File options

    @property
    def Exe(self):
        """Represents the mkdocs combine executable."""
        return self.env['Mkdocs_Combine_Exe']

    @Exe.setter
    def Exe(self, value):
        self.env['Mkdocs_Combine_Exe'] = value

    @property
    def WorkingDir(self):
        """Working directory (current directory by default)."""
        return self.env['Mkdocs_Combine_WorkingDir']

    @WorkingDir.setter
    def WorkingDir(self, value):
        self.env['Mkdocs_Combine_WorkingDir'] = value

    @property
    def Encoding(self):
        """Encoding for input files (default: utf-8)."""
        return self.env['Mkdocs_Combine_Encoding']

    @Encoding.setter
    def Encoding(self, value):
        self.env['Mkdocs_Combine_Encoding'] = value

    @property
    def Exclude(self):
        """Include files to skip (default: none)."""
        return self.env['Mkdocs_Combine_Exclude']

    @Exclude.setter
    def Exclude(self, value):
        self.env['Mkdocs_Combine_Exclude'] = value

    @property
    def OutputHtml(self):
        """If to output a single html page instead of markdown."""
        return self.env['Mkdocs_Combine_OutputHtml']

    @OutputHtml.setter
    def OutputHtml(self, value):
        self.env['Mkdocs_Combine_OutputHtml'] = value

    # Structure options

    @property
    def Meta(self):
        """If to keep YAML metadata (default), False = strip YAML metadata."""
        return self.env['Mkdocs_Combine_Meta']

    @Meta.setter
    def Meta(self, value):
        self.env['Mkdocs_Combine_Meta'] = value

    @property
    def Titles(self):
        """Add titles from mkdocs.yml to Markdown files (default).
        False = do not add titles to Markdown files."""
        return self.env['Mkdocs_Combine_Titles']

    @Titles.setter
    def Titles(self, value):
        self.env['Mkdocs_Combine_Titles'] = value

    @property
    def Uplevels(self):
        """Increase ATX header levels in Markdown files (default).
        False = do not increase ATX header levels in Markdown files."""
        return self.env['Mkdocs_Combine_Uplevels']

    @Uplevels.setter
    def Uplevels(self, value):
        self.env['Mkdocs_Combine_Uplevels'] = value

    # Table options

    @property
    def PandocTables(self):
        """True = keep original Markdown tables (default).
        False = combine Markdown tables to Pandoc-style grid tables."""
        return self.env['Mkdocs_Combine_PandocTables']

    @PandocTables.setter
    def PandocTables(self, value):
        self.env['Mkdocs_Combine_PandocTables'] = value

    @property
    def TableWidth(self):
        """Width of generated grid tables in characters (default: 100)."""
        return self.env['Mkdocs_Combine_TableWidth']

    @TableWidth.setter
    def TableWidth(self, value):
        self.env['Mkdocs_Combine_TableWidth'] = value

    # Link options

    @property
    def Refs(self):
        """True = keep MkDocs-style cross-references.
        False = replace MkDocs-style cross-references by just their title (default)."""
        return self.env['Mkdocs_Combine_Refs']

    @Refs.setter
    def Refs(self, value):
        self.env['Mkdocs_Combine_Refs'] = value

    @property
    def Anchors(self):
        """True = keep HTML anchor tags. False = strip out HTML anchor tags (default)."""
        return self.env['Mkdocs_Combine_Anchors']

    @Anchors.setter
    def Anchors(self, value):
        self.env['Mkdocs_Combine_Anchors'] = value

    # Extra options

    @property
    def MathLatex(self):
        """True = combine the \( \) Markdown math into LaTeX $$ inlines.
        False = keep \( \) Markdown math notation as is (default)."""
        return self.env['Mkdocs_Combine_MathLatex']

    @MathLatex.setter
    def MathLatex(self, value):
        self.env['Mkdocs_Combine_MathLatex'] = value

    @property
    def ImageExt(self):
        """Extension to substitute image extensions by (default: no replacement)."""
        return self.env['Mkdocs_Combine_ImageExt']

    @ImageExt.setter
    def ImageExt(self, value):
        self.env['Mkdocs_Combine_ImageExt'] = value

    @property
    def ExtraArgs(self):
        """Additional Arguments."""
        return self.env['Mkdocs_Combine_ExtraArgs']

    @ExtraArgs.setter
    def ExtraArgs(self, value):
        self.env['Mkdocs_Combine_ExtraArgs'] = value

    def set_defaults(self):
        """Set the default options"""
        self.env.SetDefault(
            # File options
            Mkdocs_Combine_Exe='mkdocscombine',
            Mkdocs_Combine_WorkingDir=self.env.Dir('.'),
            Mkdocs_Combine_Encoding=None,
            Mkdocs_Combine_Exclude=None,
            Mkdocs_Combine_OutputHtml=False,
            # Structure options
            Mkdocs_Combine_Meta=None,
            Mkdocs_Combine_Titles=None,
            Mkdocs_Combine_Uplevels=None,
            # Table options
            Mkdocs_Combine_PandocTables=None,
            Mkdocs_Combine_TableWidth=None,
            # Link options
            Mkdocs_Combine_Refs=None,
            Mkdocs_Combine_Anchors=None,
            # Extra options
            Mkdocs_Combine_MathLatex=None,
            Mkdocs_Combine_ImageExt=None,
            Mkdocs_Combine_ExtraArgs=[],
        )
