# Scons.Gbd.Docs

This is a series of builders / tools for use with Scons in relation to generating documentation.

## Example install

To install under python

```
pip install scons_gbd_docs
```

## Example useage

To use from within a SConstruct file
```python
toolpaths = [PyPackageDir('scons_gbd_docs')]
tools = ['Gbd.Docs.Mkdocs.MkdocsBuild']

env = Environment(ENV=os.environ, tools=tools, toolpath=toolpaths)

tgt = env.MkdocsBuild()
Default(tgt)
```
