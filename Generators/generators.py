#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuchang
@software: PyCharm
@file: generators.py
@time: 2020-01-28 14:30
'''
def generator_function():
    for i in range(10):
        yield i

for item in generator_function():
    print(item)