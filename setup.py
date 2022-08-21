#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name= 'pydatatest',
    version= '1.0.0',
    package_dir={"": "src"},
    packages=find_packages('src'),
    # py_modules =['api', 'data', 'common'],
    author= 'aak1247',
    author_email='aak1247@126.com',
    url='https://github.com/aak1247/PyDataTest',

    description= 'Data driven test framework',

    install_requires=[
        "pyyaml"
    ],
)