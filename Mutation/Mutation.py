#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: liuchang
@time: 2020/1/17 2:25 下午
@comments: 
'''
foo = ['hi']
print(foo)


# 每当你将一个变量赋值为另一个可变类型的变量时，对这个数据的任意改动会同时反映到这两个变量上去。
# 新变量只不过是老变量的一个别名而已。这个情况只是针对可变数据类型。
bar = foo
bar += ['hello']
print(bar)
print(foo)

def add_to(num, target=[]):
    target.append(num)
    return target

print(add_to(1))
print(add_to(2))
print(add_to(3))

