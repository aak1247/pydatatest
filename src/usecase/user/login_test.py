#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import unittest

from ...data.csv import get_data
from ...base.run_test import inject, injectable, test

data = get_data('src/data/csv/login.csv')


@test
@injectable(['passport', 'password'])
class TestUserLogin(unittest.TestCase):
    def setUp(self):
        print("登录测试开始\n")

    @inject(data[0])
    def test_01(self):
        self.assertEqual(self.passport, 'hitest')

    @inject(data[0])
    def test_02(self):
        self.assertEqual(self.password, '111111')

    def tearDown(self):
        print("登录测试结束\n")


def main():
    unittest.main()


if __name__ == '__main__':
    main()