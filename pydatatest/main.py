#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.base.run_test import test_runner
from src import usecase


@test_runner
def run(tests):
    test_suite = unittest.TestSuite()
    for test in tests:
        test_suite.addTest(unittest.makeSuite(test))
    unittest.TextTestRunner().run(test_suite)


if __name__ == '__main__':
    run()