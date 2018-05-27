import SCons.Script
from SCons.Environment import Environment
import os

EnsureSConsVersion(3, 0, 0)
env = Environment(ENV=os.environ)

AddOption('--build-templates', dest='build-templates', action='store_true', help='regenerate code from jinja templates', default=False)
AddOption('--run-tests', dest='run-tests', action='store_true', help='run the pytest tests', default=False)
AddOption('--setup-envs', dest='setup-envs', action='store_true', help='setup development python virtual environments', default=False)

# Pull in SConscript files from sub dirs
Default(None)
SConscript('scons_gbd_docs/Gbd/Docs/SConscript.py')

# Run tests
if GetOption('run-tests'):
    env.Execute('python setup.py test')

if GetOption('setup-envs'):
    env.Execute('tox -c build/tox_dev.ini')
