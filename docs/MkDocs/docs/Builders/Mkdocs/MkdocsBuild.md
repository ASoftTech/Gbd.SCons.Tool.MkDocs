# MkdocsBuild Builder


## Overview

This builder performs a straight build of an mkdocs site into html.
Typically from markdown and image files within a docs directory into a destination site directory.


## Available Settings

### Exe

  * Scons variable name: **Mkdocs_Exe**
  * Default Value: **'mkdocs'**

This setting represents the name of the mkdocs executable.


### WorkingDir

  * Scons variable name: **Mkdocs_WorkingDir**
  * Default Value: **self.env.Dir('.')**

This is for the working directory that the executable will be run within.


### CleanBuild

  * Scons variable name: **Mkdocs_CleanBuild**
  * Default Value: **None**

If to remove files from the destination site directory before building (default)


### Strict

  * Scons variable name: **Mkdocs_Strict**
  * Default Value: **False**

If to enable strict mode during the parsing of the markdown files.
Such as checking for broken links.


### Theme

  * Scons variable name: **Mkdocs_Theme**
  * Default Value: **None**

Select a different theme to use for the site
For example if you've also installed mkdocs-bootswatch you could select "cyborg"


### CustomDir

  * Scons variable name: **Mkdocs_CustomDir**
  * Default Value: **None**

This setting represents a directory that will be overlaid on top of the selected theme.
So any files in this directory will override those from the base theme


### SiteDir

  * Scons variable name: **Mkdocs_SiteDir**
  * Default Value: **None**

This represents the destination directory for the generated site.


### Quiet

  * Scons variable name: **Mkdocs_Quiet**
  * Default Value: **False**

If to silence warnings.


### Verbose

  * Scons variable name: **Mkdocs_Verbose**
  * Default Value: **False**

If to output verbose messages.


### ExcludeDirs

  * Scons variable name: **Mkdocs_ExcludeDirs**
  * Default Value: **[]**

This setting can be used as a list of directories / files to ignore when cheching for changes for the build output.
Note this only affects scons behaviour when checking for changes,
it doesn't prevent mkdocs from picking up on files / directories listed.


### ExtraArgs

  * Scons variable name: **Mkdocs_ExtraArgs**
  * Default Value: **[]**

ExtraArgs can be used to pass in any additional command line options to mkdocs
that might not be included within the configuration.
