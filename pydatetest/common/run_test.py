#! /usr/bin/env python
# -*- coding: utf-8 -*-


class InjectError(Exception):
    pass


def _inject_to(data, self):
    '''
        将数据注入测试用例类实际调用的方法
    '''
    if not self or not hasattr(self, 'title'):
        raise InjectError('function not injectable')
    for i, name in enumerate(self.title):
        setattr(self, name, data[i])


def _remove(self):
    '''
        单个测试用例完成后将注入的数据删除
    '''
    title = self.title
    for name in self.title:
        delattr(self, name)


def inject(data):
    '''
        用来注入测试用例数据
    '''
    def decorator(func):
        def wrapper(self):
            _inject_to(data, self)
            func(self)
            _remove(self)

        return wrapper

    return decorator


def injectable(title):
    if not title:
        raise InjectError('title is required')

    def decorator(klass):
        if hasattr(klass, 'title'):
            raise InjectError('title property is already used')
        return type(klass.__name__, (klass, ), {"title": title})

    return decorator


def test_runner(func):
    def decorator():
        pass


tests = []


def test(klass):
    '''
        通过注解注册测试用例类
    '''
    tests.append(klass)
    return klass


def test_runner(func):
    '''
        将测试用例传递给runner
    '''
    def decorator(*args, **kw):
        kw['tests'] = tests
        func(*args, **kw)

    return decorator

def run_test():
    import unittest
    test_suite = unittest.TestSuite()
    for test in tests:
        test_suite.addTest(unittest.makeSuite(test))
    unittest.TextTestRunner().run(test_suite)