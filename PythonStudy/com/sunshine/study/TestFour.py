print(int('123456', base = 8))

print(int('123456', 16))

def funcThirtyThree(x, base =2):
    return int(x, base)

print(funcThirtyThree('100000'))

import functools
funcThirtyFour= functools.partial(int, base=2)
print(funcThirtyFour('100000'))
print(funcThirtyFour('100001'))

print(funcThirtyFour('100000', base = 11))