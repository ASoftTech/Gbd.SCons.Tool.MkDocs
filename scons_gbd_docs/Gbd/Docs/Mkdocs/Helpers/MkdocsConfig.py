"""
Configuration class for Mkdocs
"""
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

import SCons.Script
from SCons.Environment import Environment


class MkdocsConfig:

    def __init__(self, env):
        self.env = env
        self.yamlcfg = None

    @property
    def Exe(self):
        """Represents the mkdocs executable."""
        return self.env['Mkdocs_Exe']

    @Exe.setter
    def Exe(self, value):
        self.env['Mkdocs_Exe'] = value

    @property
    def WorkingDir(self):
        """Working directory (current directory by default)."""
        return self.env['Mkdocs_WorkingDir']

    @WorkingDir.setter
    def WorkingDir(self, value):
        self.env['Mkdocs_WorkingDir'] = value

    @property
    def CleanBuild(self):
        """If to Remove old files from the site_dir before building (the default)."""
        return self.env['Mkdocs_CleanBuild']

    @CleanBuild.setter
    def CleanBuild(self, value):
        self.env['Mkdocs_CleanBuild'] = value

    @property
    def Strict(self):
        """If to enable Strict mode."""
        return self.env['Mkdocs_Strict']

    @Strict.setter
    def Strict(self, value):
        self.env['Mkdocs_Strict'] = value

    @property
    def Theme(self):
        """Which theme to use."""
        return self.env['Mkdocs_Theme']

    @Theme.setter
    def Theme(self, value):
        self.env['Mkdocs_Theme'] = value

    @property
    def ThemeDir(self):
        """Directory of additional files to merge in with the theme."""
        return self.env['Mkdocs_ThemeDir']

    @ThemeDir.setter
    def ThemeDir(self, value):
        self.env['Mkdocs_ThemeDir'] = value

    @property
    def RemoteBranch(self):
        """If to override the default remote branch setting when uploading."""
        return self.env['Mkdocs_RemoteBranch']

    @RemoteBranch.setter
    def RemoteBranch(self, value):
        self.env['Mkdocs_RemoteBranch'] = value

    @property
    def RemoteName(self):
        """If to override the default remote name setting when uploading."""
        return self.env['Mkdocs_RemoteName']

    @RemoteName.setter
    def RemoteName(self, value):
        self.env['Mkdocs_RemoteName'] = value

    @property
    def ForcePush(self):
        """If to force the push to github."""
        return self.env['Mkdocs_ForcePush']

    @ForcePush.setter
    def ForcePush(self, value):
        self.env['Mkdocs_ForcePush'] = value

    @property
    def ServeUrl(self):
        """Default is '127.0.0.1:8000'."""
        return self.env['Mkdocs_ServeUrl']

    @ServeUrl.setter
    def ServeUrl(self, value):
        self.env['Mkdocs_ServeUrl'] = value

    @property
    def LiveReload(self):
        """If to use livereload, enabled by default.
           When pages change on the file system the browser auto refreshes to show the changes"""
        return self.env['Mkdocs_LiveReload']

    @LiveReload.setter
    def LiveReload(self, value):
        self.env['Mkdocs_LiveReload'] = value

    @property
    def DirtyReload(self):
        """Enable the live reloading in the development server.
           But only re-build files that have changed"""
        return self.env['Mkdocs_DirtyReload']

    @DirtyReload.setter
    def DirtyReload(self, value):
        self.env['Mkdocs_DirtyReload'] = value

    @property
    def Quiet(self):
        """If to silence warnings."""
        return self.env['Mkdocs_Quiet']

    @Quiet.setter
    def Quiet(self, value):
        self.env['Mkdocs_Quiet'] = value

    @property
    def Verbose(self):
        """Show verbose messages."""
        return self.env['Mkdocs_Verbose']

    @Verbose.setter
    def Verbose(self, value):
        self.env['Mkdocs_Verbose'] = value

    @property
    def ExcludeDirs(self):
        """Directories to exclude for the scanner."""
        return self.env['Mkdocs_ExcludeDirs']

    @ExcludeDirs.setter
    def ExcludeDirs(self, value):
        self.env['Mkdocs_ExcludeDirs'] = value

    @property
    def ExtraArgs(self):
        """Additional Arguments."""
        return self.env['Mkdocs_ExtraArgs']

    @ExtraArgs.setter
    def ExtraArgs(self, value):
        self.env['Mkdocs_ExtraArgs'] = value

    @property
    def SiteDir(self):
        """Directory to output the build to - default is 'site'."""
        if self.env['Mkdocs_SiteDir']:
            return Dir(self.env['Mkdocs_SiteDir'])
        elif 'site_dir' in self.yamlcfg:
            return Dir(self.yamlcfg['site_dir'])
        else:
            return Dir('site')

    @SiteDir.setter
    def SiteDir(self, value):
        self.env['Mkdocs_SiteDir'] = value

    @property
    def DocsDir(self):
        """doc Source directory, can only be set in the yaml config file."""
        if 'docs_dir' in self.yamlcfg:
            docsdirnode = Dir(self.yamlcfg['docs_dir'])
        else:
            docsdirnode = Dir('docs')
        return docsdirnode

    def read_cfg(self, cfgfile):
        """Read the mkdocs yaml configuration file"""
        with open(str(cfgfile), 'r') as stream:
            self.yamlcfg = yaml.load(stream)

    def set_defaults(self):
        """Set the default options"""
        env.SetDefault(
            Mkdocs_Exe='mkdocs',
            Mkdocs_WorkingDir=env.Dir('.'),
            Mkdocs_CleanBuild=None,
            Mkdocs_Strict=False,
            Mkdocs_Theme=None,
            Mkdocs_ThemeDir=None,
            Mkdocs_RemoteBranch=None,
            Mkdocs_RemoteName=None,
            Mkdocs_ForcePush=False,
            Mkdocs_ServeUrl=None,
            Mkdocs_LiveReload=None,
            Mkdocs_DirtyReload=False,
            Mkdocs_Quiet=False,
            Mkdocs_Verbose=False,
            Mkdocs_ExcludeDirs=[],
            Mkdocs_ExtraArgs=[],
        )
