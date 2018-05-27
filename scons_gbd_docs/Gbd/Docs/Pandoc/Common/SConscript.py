import SCons.Script
from SCons.Environment import Environment

import os
import yasha.scons

env = Environment(
    ENV=os.environ,
    BUILDERS={"Yasha": yasha.scons.Builder(action="yasha --no-extension-file -o $TARGET $SOURCE")}
)

template_tgts = env.Yasha(["PandocConfig.py.j2"])

if GetOption('build-templates'):
    Default(template_tgts)
