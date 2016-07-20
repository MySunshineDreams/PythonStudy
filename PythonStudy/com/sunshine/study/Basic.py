#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Python基础'

# Python基础

# hello world
print('hello world')

# print()函数也可以接受多个字符串
print('I', 'am', 'a', 'coder')

# 输入
name = input()

print(name)

# 条件语句
age = 22

if 0 < age <= 18:
    print('未成年')
elif 18 < age <= 28:
    print('青年')
elif 28 < age <= 60:
    print('中年')
