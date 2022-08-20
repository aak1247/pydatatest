#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

class Runner(object):
    '''
    Runner instance
    '''
    def __init__(self):
        self._pydatatest_tests = []

    def run(self):
        test_suite = unittest.TestSuite()
        for test in self._pydatatest_tests:
            test_suite.addTest(unittest.makeSuite(test))
        unittest.TextTestRunner().run(test_suite)

def runner():
    '''
    get a runner
    '''
    return Runner()


def run_with(runner):
    '''
    declare a testcase that will run with a Runner
    '''
    def decorator(klass):
        klass._pydatatest_runner = runner
    return decorator



def test(klass):
    '''
    register a testcase class or method
    TODO: method
    '''
    runner = klass._pydatatest_runner
    runner.tests.append(klass)
    return klass


def test_runner(runner):
    '''
    pass test data to customised runner
    '''
    def decorator(func):
        def wrapper(*args, **kw):
            kw['__tests'] = func.self._pydatatest_runner.tests
            func(*args, **kw)
        return wrapper
    return decorator
