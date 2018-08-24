#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Maksim Vasilev'


from cx_Freeze import setup, Executable

base = None

executables = [Executable("game.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name = "<any name>",
    options = options,
    version = "1.0",
    description = '<any description>',
    executables = executables, requires=['pygame']
)