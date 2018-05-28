# MkdocsConfig


## Accessing Settings

The builders associated with mkdocs can be configured in two different ways.

  * The conventional method for scons to store it's settings is within an environment object / dictionary
  * A wrapper python class that can also be accessed from the environment


### Settings via the scons environment

For the conventional method.

```python
# Setup an environment
tools = ['Gbd.Docs.Mkdocs']
toolpaths = [PyPackageDir('scons_gbd_docs')]
env = Environment(ENV=os.environ, tools=tools, toolpath=toolpaths)

# Change some settings
env.Replace(Mkdocs_SiteDir = "site2")
```


### Settings via the wrapper class

The wrapper class actually reads / writes to the scons environment dictionary under the hood. <br>
An instance of it is created during the generate / setup of the tool automatically and can be accessed via `env['Mkdocs_Config']` <br>
The assert statement allows for an IDE such as Visual Studio code to add intellisense to the cfg variable.

```python
# Setup an environment
tools = ['Gbd.Docs.Mkdocs']
toolpaths = [PyPackageDir('scons_gbd_docs')]
env = Environment(ENV=os.environ, tools=tools, toolpath=toolpaths)

# Access the wrapper class
cfg = env['Mkdocs_Config']
assert isinstance(cfg, MkdocsConfig)

# Change some settings
cfg.SiteDir = "site2"
```
