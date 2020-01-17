#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: liuchang
@time: 2020/1/17 2:09 下午
@comments: 
'''

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']


duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
print(set(x for x in some_list if some_list.count(x) > 1))


# 你可以用差集(difference)找出无效的数据，相当于用一个集合减去另一个集合的数据，例如：
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.difference(valid))


# 你也可以用{}符号来创建集合，如：
a_set = {'red', 'blue', 'green'}
print(type(a_set))



