#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'正则表达式'

#正则表达式

import re

print(re.match(r'^\d{3}\-\d{3,8}$', '010-58323211'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010-583232111'))

#常见的正则表达式判断方法
telephoneNumber = '010-58323211'

if re.match(r'^\d{3}\-\d{3,8}$', telephoneNumber):
	print('It is a telephone number.')
else:
	print('It is not a telephone number')

#切分字符串
strOne = 'ab  c'
print(strOne.split(' '))

print(re.split(r'\s+', strOne))

print(re.split(r'[\s\,]+', 'a,b, c  d'))

print(re.split(r'[\s\,\:]', 'a,b,:c d'))

m = re.match(r'^(\d{3})-(\d{3,8})', '010-87654321')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))

#时间校验
time = '22:40:55'

m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', time)
print(m.groups())

#贪婪匹配
print(re.match(r'^(\d+)(0*)$', '1230000').groups())

#禁止贪婪匹配
print(re.match(r'^(\d+?)(0*)$', '1230000').groups())

#正则表达式预编译
import re

#编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
#使用
# print(re_telephone.match('010-87654321').groups())
# print(re_telephone.match('010-987654321').groups())

#练习
#请尝试写一个验证Email地址的正则表达式
#1.应该可以验证出类似的Email
#2.可以验证并提取出带名字的Email地址
regexOne = r'^[0-9a-zA-Z]+@(\w+).([com|cn|net|org])$'
regexTwo = r'^(<[a-zA-Z]>)[0-9a-zA-Z]+@(\w+).([com|cn|net|org])$'