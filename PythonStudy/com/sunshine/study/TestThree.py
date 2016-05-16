from functools import reduce
def funcOne():
    print('1')
    yield 1
    print('2')
    yield 2
    print('3')
    yield 3

a = funcOne()
print(next(a))

def funcTwo(n):
    if n % 2 != 0:
        return n

print(list(map(funcTwo, [1, 2, 3, 4, 5, 6])))

def funcNine(str):
    n = 0
    x = ''
    for s in str:
        if n == 0:
            n += 1
            x += s.upper()
        else:
            n += 1
            x += s.lower()
    return x
L1 = ['adam', 'LISA', 'barT']

print(list(map(funcNine, L1)))

from functools import  reduce

def funcTen(Lp):
    sum = 1
    for n in Lp:
       sum = sum * n
    return sum

print(funcTen([3, 5, 7, 9]))


def funcTwelve(s1):
    a = s1.split('.')
    if len(a) != 2:
        return None
    s1 = s1.replace('.', '')
    s1len = len(a[1])
    def funcThirteen(s2, s3):
        return 10 * s2 + s3
    def funcFourteen(s5):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s5]
    a = reduce(funcThirteen, map(funcFourteen, s1))
    n = 1
    while s1len > 0:
        n = n * 10
        s1len -= 1
    return a / n

print(funcTwelve('123.456'))

def funcFifteen(n):
    return n % 2 == 1

print(list(map(funcTwo, [1, 2, 3, 4, 5, 6])))

def funcSixteen(n):
    return n % 2 == 1
print(list(filter(funcSixteen, [1, 2, 3, 4, 5, 6])))

def funcSeventeen(x):
    return x and x.strip()

print(list(filter(funcSeventeen, ['A', '', 'B', None, 'C', '  '])))

def funcEighteen():
    n = 3
    while True:
        yield n
        n = n + 2

fe = funcEighteen()
print(next(fe))
print(next(fe))
print(next(fe))

def funcNineteen(n):
    return lambda x : x % n > 0

def funcTwenty():
    yield 2
    it = funcEighteen()
    while True:
        n = next(it)
        yield n
        it = filter(funcNineteen(n), it)

for n in funcTwenty():
    if n < 1000:
        print(n)
    else:
        break

def funcTwentyOne(n):
    return str(n)[::-1]
print(list(filter(funcTwentyOne, range(1, 1000))))

def funcTwentyTwo(n):
    s = str(n)
    if len(s) == 1 or len(s) == 2:
        if s[0] == s[-1]:
            return True
        else:
            return False
    elif s[0] == s[-1]:
        return funcTwentyTwo(s[1:-1])
    else:
        return False

print(list(filter(funcTwentyTwo, range(1, 1001))))

#排序
print(sorted([36, 5, -12, 9, -21]))

print(sorted([36, 5, -12, 9, -21], key = abs))

#排序字符串
print(sorted(['bob', 'about', 'Zoo', 'Credit']))

#忽略大小写排序字符串
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower))

#反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse = True))

#小练习
T = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def funcTwentyThree(t):
    return t[0]

def funcTwentyFour(t):
    return t[1]

def funcTwentyFive(t):
    return t[1] * -1



print(sorted(T, key = funcTwentyThree))

print(sorted(T, key = funcTwentyFour))

print(sorted(T, key = funcTwentyFive))

print(sorted(T, key = funcTwentyFour, reverse = True))

#函数返回函数
def funcTwentySeven(*args):
    def sum():
        plusSum = 0
        for n in args:
            plusSum += n
        return plusSum
    return sum

fts1 = funcTwentySeven(1, 3, 5, 7, 9)
fts2 = funcTwentySeven(1, 3, 5, 7, 9)

print(fts1 == fts2)

#闭包
def funcTwentyEight():
    fte1 = []
    for i in range(1, 4):
        def funcTwentyEightOne():
            return i * i
        fte1.append(funcTwentyEightOne)
    return fte1

fte2, fte3, fte4 = funcTwentyEight()

print(fte2(), fte3(), fte4())

def funcTwentyNine():
    def funcTwentyNineOne(j):
        def funcTwentyNineTwo():
            return j * j
        return funcTwentyNineTwo
    ftn1 = []
    for i in range(1, 4):
        ftn1.append(funcTwentyNineOne(i))
    return ftn1

ftn2, ftn3, ftn4 = funcTwentyNine()

print(ftn2(), ftn3(), ftn4())

#lambda函数
print(list(map(lambda x : x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

def funcThirtyOne(x, y):
    return lambda : x * x + y * y

#装饰器
def funcThirtyTwo():
    print('2015-12-06')
ftt1 = funcThirtyTwo
print(ftt1())

print(funcThirtyTwo.__name__)

print(ftt1.__name__)

def funcLog(func):
    def wrapper(*args, **keywords):
        print('call %s():' % func.__name__)
        return func(*args, **keywords)

    return wrapper

def funcLogOne(text):
    def decorator(func):
        def wrapper(*args, **keyword):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **keyword)
        return wrapper
    return decorator

@funcLogOne('execute')
def funcThirtyTwo():
    print('2015-12-07')

print(funcThirtyTwo())

funcThirtyTwo = funcLogOne('execute')(funcThirtyTwo)

print(funcThirtyTwo.__name__)

import  functools

def funcLogThree(func):
    @functools.wraps(func)
    def wrapper(*args, **keyword):
        print('call %s()', func.__name__)
        return func(*args, **keyword)
    return wrapper

import  functools

def funcLogFour(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **keyword):
            print('$s $s()' % (text, func.__name__))
        return wrapper
    return decorator