#! /usr/bin/env python
# -*- coding: utf-8 -*-

import yaml


def get_data():
    data = {}
    with open('data/data.yml', 'r') as data_yml:
        data = yaml.load(data_yml)
    return data
