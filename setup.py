#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

from LabIFSC import __version__ as version

setup(name='LabIFSC',
    version=version,
    description='Uma biblioteca para automatizar tarefas ligadas às disciplinas de laboratório de física do IFSC-USP (Python 2 e Python 3)',
    author='Gabriel Queiroz',
    author_email='gabrieljvnq@gmail.com',
    url = 'https://github.com/gjvnq/LabIFSC',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['LabIFSC'],
    keywords = ['uncertainty propagation', 'unit conversion'],
    classifiers=[
    	"Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: tox",
        "Intended Audience :: Education",
        "Natural Language :: Portuguese (Brazilian)",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Utilities"
    ],
)
