#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Python函数'

def funcOne(*numbers) :
    sum = 0
    for n in numbers :
        sum = sum + n * n
    return sum

print(funcOne(1, 2, 3))

def funcTwo(name, age, **keyword) :
    print(name, age, 'others:', keyword)

print(funcTwo('yangsl', 22, city = 'Beijing', work = 'Engineer'))

def funcThree(name, age, *, city, work) :
    print('name:', name, ' age:', age, 'city:', city, ' work:', work)

print(funcThree('yangsl', 22, city = 'Beijing', work = 'Engineer'))

def funcFour(name, age, *, city = 'Beijing', work = 'Engineer') :
    print('name:', name, ' age:', age, 'city:', city, ' work:', work)

print(funcFour('yangsl', 22))

L = list(range(100))

print(L)

print(L[:10])

print(L[::5])

T = tuple(range(100))

print(T)

print(T[::5])

print(T[-10::2])

dict = {'1' : 'yangsl', '2' : 'wangshiyue', '3' : 'zhaohe'}

for value in dict.values() :
    print(value)

for key in dict :
    print(key)

s = 'yangsl'

for str in s :
    print(str)

from collections import  Iterable

print(isinstance('abc', Iterable))

print(isinstance(dict, Iterable))

for i, value in enumerate(L) :
    print(i, value);

print([x * x for x in range(1, 11)])

print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in 'Yangsl' for n in 'Zhangyuhong'])

d = {'x' : 'A', 'y' : 'B', 'z' : 'C'}

for k, v in d.items() :
    print(k, '=', v)

print([k + '=' + v for k, v in d.items()])

L = ['HELLO', 'WORLD', 'JAVA', 'PHP', 'NODEJS']

print([s.lower() for s in L])

L1 = ['Hello', 'World', 18, 'Apple', None]

print([s.lower() for s in L1 if isinstance(s, str)])