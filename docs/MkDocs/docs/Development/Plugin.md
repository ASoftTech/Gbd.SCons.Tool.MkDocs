# Plugin

## Overview

These are just some notes for myself for an implementation for loading in tools for scons via setup entry points

  * https://stackoverflow.com/questions/774824/explain-python-entry-points
  * http://amir.rachum.com/blog/2017/07/28/python-entry-points/


I've setup a couple of my own repos with tools in that should implement this
```
# https://github.com/ASoftTech/Scons.Gbd.Docs
pip install git+https://github.com/ASoftTech/Scons.Gbd.Docs

# https://github.com/ASoftTech/Scons.Gbd.Builders
pip install git+https://github.com/ASoftTech/Scons.Gbd.Builders
```

This Scons repo that will eventually include the plugin entry points support

  * https://github.com/grbd/scons.git



## How it works

There's no userdocs or man pages written for this yet so this is just a rough overview


### Load in of Entry points

The first step is that scons has to scan for any available plugins via entry points
There is a new package called scons\src\engine\SCons\Plugin.py

One of the functions is called at startup of scons, and scans through setup entry points for 'scons.plugins'

On the plugin side there will be an entry within setup.py similar to this
```
    entry_points={
        'scons.plugins': [
            'scons_gbd_docs=scons_gbd_docs.plugin:scons_gbd_docs',
        ]
    }
 ```

This will return a class called **scons_gbd_docs** within the package **scons_gbd_docs/plugin.py**
This class should inherit from the **SconsBasePlugin** base class located within the scons Plugin.py

TODO will this be an issue?
can we access **SconsBasePlugin** during the plugin load phase, since Scons code isn't visible outside of scons.


### Plugin hooks

There are two functions get_metadata() and on_tool_load()

The get_metadata function just returns information about the plugin such as description / name / author
```
    def get_metadata(self):
        """return metadata associated with the plugin"""
        self.metadata = {
            'name' = 'scons_gbd_docs',
            'description' = 'Documentation tools for use with SCons, e.g. MkDocs, Doxygen',
            'author' = 'grbd'}
        return self.metadata
```
The on_tool_load function returns a tuple of the associated namespace and the directory of the toolpath
```
    def on_tool_load(self):
        """return a list of namespace / toolpath pairs"""
        # Test multiple toolspecs
        tools =
        [
            {'namespace': 'Gbd.Docs',
             'toolpath': PyPackageDir('scons_gbd_docs.Gbd.Docs').abspath},
        ]
        self.toolspecs = tools
        return self.toolspecs
```

### Load in of tools

At this point the plugin code within scons creates a list of namespace and directory path for all plugins.

  * there should be a command line option to show all plugins loaded in short form or long form with metadata
  * there should also be a command line option to prevent specific plugins from being loaded, or perhaps to manually add in plugins.
  * perhaps an enable / disable option?

When the user asks for a tool, the plugin code can compare the namespace name
to see if the requested tool starts with that namespace as an initial match.
e.g. 'Gbd.Docs' matches when 'Gbd.Docs.Mkdocs' is asked for

the search order should be

  * toolpath specified by user
  * plugin toolpath if the namespace matches
  * builtin scons tools

### Testing

not sure how to test the plugin loader code without any plugins
(a bit of a chicken and egg situation)
