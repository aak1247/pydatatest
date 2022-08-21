#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import unittest

from usecase.runner import myrunner

from pydatatest.util.csv import get_data
from pydatatest.api import inject, inject_def, test, PyDataTestCase, test_with

data = get_data('examples/data/csv/login.csv')


@inject_def(['passport', 'password'], session=True)
@test_with(myrunner)
class TestUserLogin(PyDataTestCase):
    @classmethod
    def before_all(cls):
        print("before all test")

    @classmethod
    def after_all(cls):
        print("after all test")

    def before_each(self):
        print("before_each test")
    
    def after_each(self):
        print("after_each test")

    def before_each_data(self):
        print("before_each_data test")
    
    def after_each_data(self):
        print("after_each_data test")


    @inject(data[0])
    def test_01(self):
        self.assertEqual(self.passport, 'username')

    @inject(data, multi=True)
    def test_02(self):
        print(self.passport)
        print(self.password)
        self.assertEqual(self.password, 'password')

    @inject(["username", "password1"])
    def test_03(self):
        self.assertEqual(self.password, 'password')

def main():
    unittest.main()


if __name__ == '__main__':
    main()