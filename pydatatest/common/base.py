#! /usr/bin/env python
# -*- coding: utf-8 -*-


class InjectError(Exception):
    pass


class TestError(Exception):
    pass


def _inject_to(data, self):
    '''
        将数据注入测试用例类实际调用的方法
    '''
    if not self or not hasattr(self, '_title'):
        raise InjectError('function not injectable')
    for i, name in enumerate(self._title):
        setattr(self, name, data[i])


def _inject_multi_to(dataset, self):
    '''
        将多组数据注入同一个测试用例
    '''
    if not self or not hasattr(self, '_title'):
        raise InjectError('function not injectable')
    if len(dataset) > 1:
        data = dataset[0]
        self._dataset = dataset[1:]
        self._multi = True
    else:
        data = dataset[0]
        self._dataset = None
        self._multi = False
    for i, name in enumerate(self._title):
        setattr(self, name, data[i])


def _remove(self):
    '''
        单个测试用例完成后将注入的数据删除
    '''
    _title = self._title
    for name in self._title:
        delattr(self, name)


def inject(data, multi=False):
    '''
        用来注入测试用例数据
    '''
    def decorator(func):
        def wrapper(self):
            if multi:
                _inject_multi_to(data, self)
            else:
                _inject_to(data, self)
            func(self)
            _remove(self)

        return wrapper

    return decorator


def injectable(title=[], session=False):
    import requests

    def setUpSession(func, klass):
        def decorator(*args, **kw):
            klass.session = requests.Session()
            func(*args, **kw)

        return decorator

    def tearDownSession(func, klass):
        def decorator(*args, **kw):
            klass.session.close()
            func(*args, **kw)

        return decorator

    def decorator(klass):
        if session:
            klass.setUp = setUpSession(klass.setUp, klass)
            klass.tearDown = tearDownSession(klass.tearDown, klass)
        return type(klass.__name__, (klass, ), {"_title": title})

    return decorator

tests = []


def test(klass):
    '''
        通过注解注册测试用例类
    '''
    tests.append(klass)
    return klass



import unittest

class HiveTestCase(unittest.TestCase):
    '''test base case
    '''
    def __init__(self, methodName):
        super().__init__(methodName)
        self._multi = False
        self._dataset = []

    def run(self, result=None):
        if result is not None:
            if hasattr(result, 'dots'):
                result.dots = False
        if (self._multi):
            for i in len(self._dataset):
                _inject_multi_to(self._dataset, self)
                super().run(result)
        else:
            super().run(result)