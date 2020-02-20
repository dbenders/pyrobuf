"""Setuptools integration."""
from pyrobuf.compile import Compiler

try:
    basestring
except NameError:
    # Python 3.x
    basestring = str

import sys
import os
if sys.version_info.major == 3:
    _FileExistsError = FileExistsError
else:
    _FileExistsError = OSError


def add_pyrobuf_module(dist, pyrobuf_module, args):
    dir_name = "pyrobuf/_" + pyrobuf_module
    package = "{}_{}".format(dist.get_name(), pyrobuf_module)
    try:
        os.makedirs(os.path.join(dir_name, package))
    except _FileExistsError:
        pass

    compiler = Compiler([pyrobuf_module], out=dir_name,
                        package=package, **args)
    compiler.extend(dist)


def pyrobuf(dist, attr, value):
    assert attr == 'pyrobuf'

    args = value.get('args', {})
    for pyrobuf_module in value.get('modules', []):
        add_pyrobuf_module(dist, pyrobuf_module, args)

