L1 = ['Hello', 'World', 18, 'Apple', None]

print([s.lower() for s in L1 if isinstance(s, str)])

H = [x * x for x in range(11)]

print(H)

I = (x * x for x in range(11))

print(I)

print(next(I))

for n in I :
    print(n)

#斐波那契数列
def funcOne(max) :
    n, a, b = 0, 1, 1
    while n < max :
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

print(funcOne(10))

def funcTwo(max) :
    n, a, b = 0, 1, 1
    while n < max :
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

print(funcTwo(10))

def funcThree():
    print('11')
    yield 'this is 1'
    print('22')
    yield 'this is 2'
    print('33')
    yield 'this is 3'
a = funcThree()

next(a)
next(a)
next(a)
#          1
#        1   1
#      1   2   1
#    1   3   3   1
#  1   4   6   4   1
#1   5   10  10  5   1
def triangles():
    l = [1]
    yield(l)
    l = [1,1]
    yield l
    while True:
        l1 = l[1:]
        for n in range(len(l1)):
            l[n] = l1[n]+l[n]
        l = [1]+l
        yield l
next(triangles())