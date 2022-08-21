#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import functools


class Http():
    def post(self, url, data, headers=[]):
        result = requests.post(url=url, data=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def get(self, url, params, headers=[]):
        result = requests.get(url=url, params=params).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res


def need_login(login_func):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            login_func()
            return func(*args, **kw)

        return wrapper

    return decorator
