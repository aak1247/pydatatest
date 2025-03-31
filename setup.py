#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf8').read()

setup(
    name= 'pydatatest',
    version= '1.0.6',
    package_dir={"": "src"},
    packages=find_packages('src'),
    # py_modules =['api', 'data', 'common'],
    author= 'aak1247',
    author_email='aak1247@126.com',
    url='https://github.com/aak1247/PyDataTest',
    description= 'Data driven test framework',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    install_requires=[
        "pyyaml",
        #"requests", # optional, only if you want to use session, it is needed
    ],
)