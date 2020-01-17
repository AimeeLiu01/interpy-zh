#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: liuchang
@time: 2020/1/17 2:37 下午
@comments: 
'''
number_list = range(-5, 5)
less_than_zero = filter(lambda x: x < 0, number_list)
print(list(less_than_zero))

