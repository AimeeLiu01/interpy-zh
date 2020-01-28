#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: liuchang
@time: 2020/1/17 2:57 下午
@comments: 
'''
# tuple(元组)，list(列表)或者dict(字典)

def profile():
    name = "Danny"
    age = 30
    return (name, age)

profile_data = profile()
print(profile_data[0])
print(profile_data[1])
print(type(profile_data))

def profile1():
    name = "Danny"
    age = 30
    return name, age

print(profile1())
print(type(profile1()))


