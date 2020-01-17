#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: liuchang
@time: 2020/1/17 2:18 下午
@comments: 
'''
# open的第一个参数是文件名。第二个(mode 打开模式)决定了这个文件如何被打开。
#
# 如果你想读取文件，传入r
# 如果你想读取并写入文件，传入r+
# 如果你想覆盖写入文件，传入w
# 如果你想在文件末尾附加内容，传入a

import io

with open('test.txt', 'rb') as inf:
    testdata = inf.read()

if testdata.startswith(b'\xff\xd8'):
    text = u'This is a JPEG file (%d bytes long)\n'
else:
    text = u'This is a random file (%d bytes long)\n'

with io.open('summary.txt', 'w', encoding='utf-8') as outf:
    outf.write(text % len(testdata))
