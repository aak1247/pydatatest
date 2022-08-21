#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
This package is to provide use usable interfaces
'''

from pydatatest.common.testcase import PyDataTestCase

from pydatatest.common.inject import inject_def
from pydatatest.common.inject import inject
from pydatatest.common.inject import InjectError


from pydatatest.common.runner import runner
from pydatatest.common.runner import test_with
from pydatatest.common.runner import test
from pydatatest.common.runner import test_runner



# testcase = PyDataTestCase # a signle test case


# def test_with():
#     '''
#     indicates the runner which will run current testcase\
#     '''
#     pass

# def test():
#     '''
#     register a testcase
#     '''
#     pass