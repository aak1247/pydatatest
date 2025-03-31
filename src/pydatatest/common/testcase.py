#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from pydatatest.common.inject import _inject_multi_to


class TestError(Exception):
    pass


class PyDataTestCase(unittest.TestCase):
    '''test base case
    '''
    def __init__(self, methodName):
        super().__init__(methodName)
        self._pydatatest_runner = None
        self._pydatatest_multi = False
        self._pydatatest_dataset = []

    @classmethod
    def before_all(cls):
        '''
        before all tests
        '''
        pass

    @classmethod
    def after_all(cls):
        '''
        after all tests
        '''
        pass
    
    def before_each(self):
        '''
        run before each test method
        '''
        pass

    def after_each(self):
        '''
        run after each test method
        '''
        pass
    
    def before_each_data(_self):
        '''
        run before each test data
        '''
        pass

    def after_each_data(self):
        '''
        run after each test data
        '''
        pass

    def run(self, result=None):
        '''
        run a testcase method
        '''
        self.before_each()
        e = None
        if result is not None:
            if hasattr(result, 'dots'):
                result.dots = False

        self.before_each_data()
        super().run(result)
        self.after_each_data()

        if (self._pydatatest_multi):
            for i in range(len(self._pydatatest_dataset)):
                self.before_each_data()
                super().run(result)
                self.after_each_data()
        
        self.after_each()
        if e is not None:
            raise TestError(e)

    @classmethod
    def setUpClass(cls):
        cls.before_all()

    @classmethod
    def tearDownClass(cls):
        cls.after_all()
