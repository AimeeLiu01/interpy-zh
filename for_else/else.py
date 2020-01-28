#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuchang
@software: PyCharm
@file: else.py
@time: 2020-01-28 14:26
'''

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n / x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')