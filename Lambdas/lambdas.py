#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: liuchang
@time: 2020/1/17 2:47 下午
@comments: 
'''
# lambda表达式是一行函数。
# 它们在其他语言中也被称为匿名函数。如果你不想在程序中对一个函数使用两次，你也许会想用lambda表达式，它们和普通的函数完全一样。

add = lambda x, y: x + y
print(add(4,5))


# 列表排序
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[0])
print(a)

# 列表并行排序
list1 = [1,11,3,9,5]
list2 = [2,10,8]
data = zip(list1, list2)
data = sorted(data)
list1, list2 = map(lambda t: list(t), zip(*data))
print(list1, list2)
