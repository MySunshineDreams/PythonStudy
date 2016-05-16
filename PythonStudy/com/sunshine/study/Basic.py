#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Python基础'

# Python基础

# hello world
print('hello world')

# print()函数也可以接受多个字符串
print ('I', 'am', 'a', 'coder')

# 输入
name = input()
name
print(name)

# 条件语句
age = 22

if 0 < age <= 18:
    print('未成年')
else if 18 < age <= 28 : 
    print('青年')
else if 28 < age <= 60 :
    print('中年')
else if age > 60 :
    print('老年')