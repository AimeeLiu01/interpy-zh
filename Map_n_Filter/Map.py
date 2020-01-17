#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: liuchang
@time: 2020/1/17 2:40 下午
@comments: 
'''
import numpy as np
import pandas as pd

items = [1, 2, 3, 4, 5]
print(type(items))
item_arr = np.array(items)
print(type(item_arr))

squared = []
for i in items:
    squared.append(i**2)

# 大多数时候，我们使用匿名函数(lambdas)来配合map, 不仅用于一列表的输入， 我们甚至可以用于一列表的函数
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)


