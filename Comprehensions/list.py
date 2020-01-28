#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuchang
@software: PyCharm
@file: list.py
@time: 2020-01-28 14:11
'''
multiples = [i for i in range(30) if i % 3 is 0]
print(multiples)

squared = []
for x in range(10):
    squared.append(x**2)
print(squared)