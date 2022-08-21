#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from common.inject import _inject_multi_to


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
        e = None
        self.before_each()
        if result is not None:
            if hasattr(result, 'dots'):
                result.dots = False
        if (self._pydatatest_multi):
            for i in len(self._pydatatest_dataset):
                _inject_multi_to(self._pydatatest_dataset, self)
                self.before_each_data()
                try:
                    super().run(result)
                except Exception as e:
                    break
                self.after_each_data()
        else:
            self.before_each_data()
            try:
                super().run(result)
            except Exception as e:
                pass
            self.after_each_data()
        self.after_each()
        if e is not None:
            raise TestError(e)

