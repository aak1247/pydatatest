#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import unittest

from pydatatest.data.csv import get_data
from pydatatest.common.base import inject, injectable, test

data = get_data('src/data/csv/login.csv')


@test
@injectable(['passport', 'password'])
class TestUserLogin(unittest.TestCase):
    def setUp(self):
        print("login test start\n")

    @inject(data[0])
    def test_01(self):
        self.assertEqual(self.passport, 'hitest')

    @inject(data[0])
    def test_02(self):
        self.assertEqual(self.password, '111111')

    def tearDown(self):
        print("login test end\n")


def main():
    unittest.main()


if __name__ == '__main__':
    main()