#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from pydatatest.common import testcase
from pydatatest.util.inspect import retrieve_name


class Runner(object):
    '''
    Runner instance
    '''
    def __init__(self, name):
        self._pydatatest_tests = []
        self._pydatatest_name = name

    def run(self):
        test_suite = unittest.TestSuite()
        for test in self._pydatatest_tests:
            test_suite.addTest(unittest.makeSuite(test))
        unittest.TextTestRunner().run(test_suite)

    def add_test(self, test):
        if not isinstance(test, testcase.PyDataTestCase):
            raise Exception("type mismatch: expected to be a PyDataTest")
        self._pydatatest_tests.append(test)


runners = {}


def runner(name = ""):
    '''
    get a runner
    '''
    if not name:
        name = retrieve_name(name)
        if not name:
            import random
            import string
            name = 'runner_' + ''.join(random.sample(string.ascii_letters + string.digits, 10)) #生成5位随机字符，包括大小写字母和数字
    r = Runner(name)        
    runners.__setitem__(name, r)
    return r


def run_with(runner):
    '''
    declare a testcase that will run with a Runner
    '''
    if type(runner) == str:
        runner = runners.__getitem__(runner)
    def decorator(klass):
        klass._pydatatest_runner = runner
        return klass
    return decorator


def test(klass):
    '''
    register a testcase class or method
    '''
    runner = klass._pydatatest_runner
    runner._pydatatest_tests.append(klass)
    return klass


def test_runner(runner):
    '''
    pass test data to customised runner
    '''
    def decorator(func):
        def wrapper(*args, **kw):
            kw['_pydatatest_tests'] = func.self._pydatatest_runner.tests
            func(*args, **kw)
        return wrapper
    return decorator