#! /usr/bin/env python
# -*- coding: utf-8 -*-

import csv


def get_data(file_name):
    data = []
    with open(file_name, 'r') as csv_file:
        data = list(csv.reader(csv_file, delimiter=' '))
    return data