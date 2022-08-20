#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
This package is to provide use usable interfaces
'''

from common.testcase import PyDataTestCase

from common.inject import inject_def
from common.inject import inject
from common.inject import InjectError


from common.runner import runner
from common.runner import run_with
from common.runner import test
from common.runner import test_runner



# testcase = PyDataTestCase # a signle test case


# def run_with():
#     '''
#     indicates the runner which will run current testcase\
#     '''
#     pass

# def test():
#     '''
#     register a testcase
#     '''
#     pass