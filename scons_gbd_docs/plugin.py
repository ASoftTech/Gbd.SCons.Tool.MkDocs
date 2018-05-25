"""
Used by scons on startup to look for plugins / tools
"""

from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

from Scons.Plugins import BasePlugin


class GbdDocTools(SconsBasePlugin):


    def get_metadata(self)
        """return metadata associated with the plugin"""
        self.metadata = {
            'name' = 'scons_gbd_docs',
            'api' = '1.0.0',
            'description' = 'Documentation tools for use with SCons, e.g. MkDocs, Doxygen',
            'author' = 'grbd'
            }
        return self.metadata


# Test single toolspec
#    def on_tool_load(self):
#        """return a list of namespace / toolpath pairs"""
#        tool = {
#                'namespace': 'Gbd.Docs',
#                'toolpath': PyPackageDir('scons_gbd_docs.Gbd.Docs').abspath,
#               }
#        self.toolspecs = [tool]
#        return self.toolspecs


# Test multiple toolspecs
    def on_tool_load(self):
        """return a list of namespace / toolpath pairs"""
        tools = [{
                  'namespace': 'Gbd.Docs.Mkdocs',
                  'toolpath': PyPackageDir('scons_gbd_docs.Gbd.Docs.Mkdocs').abspath,
                 },
                 {
                  'namespace': 'Gbd.Docs.Doxygen',
                  'toolpath': PyPackageDir('scons_gbd_docs.Gbd.Docs.Doxygen').abspath,
                 }]
        self.toolspecs = tools
        return self.toolspecs
