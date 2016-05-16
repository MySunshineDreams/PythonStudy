#! /usr/bin/envy python3
# -*- code utf-8 -*-

'面向对象编程'
class Student(object):
    def __init__(self, name):
        self.name = name

stu = Student('Sunshine')
stu.score = '150'

#类中定义属性
class Student(object):
    name = 'Sunshine'

#类属性访问范围测试
s = Student()   #创建实例
print(s.name)   #打印name属性，因为实例没有name属性，所以打印Student的name属性
print(Student.name) #打印Student类的name属性
s.name = 'Yang' #给实例绑定name属性
print(s.name)   #打印实例的name属性
print(Student.name) #打印Student类的name属性
del s.name  #删除实例的name属性
print(s.name)   #打印实例的name属性

#声明class
class Student(object):
    pass

#尝试给Student绑定属性
stu = Student()
stu.name = 'Sunshine'
print(s.name)

#尝试给实例绑定方法
def setName(self, name):
    self.name = name

from types import MethodType
stu.setName = MethodType(setName, stu)
stu.setName('Yang')
print(stu.name)

#给对象绑定方法
from types import MethodType
Student.setName = MethodType(setName, Student)
stuOne = Student()
stuOne.setName('Yang')
print(stuOne.name)

#使用__slots__限制class实例能添加的属性
class Student(object):
    __slots__ = ('name', 'age') #使用tuple定义允许绑定的属性名称

stuTwo = Student()
#stuTwo.score = 99
#print(stuTwo.score)

#__slots__对类的子类没有效果
class SeniorStudent(Student):
    pass

seniorStudent = SeniorStudent()
seniorStudent.score = 100
print(seniorStudent.score)

#封装Student
class Student(object):
    def getScore(self):
        return self._score

    def setScore(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an Integer')
        if value < 0 or value >150:
            raise ValueError('Score must be 0 ~ 150')
        self._score = value

newStu = Student()
newStu.setScore(150)
print(newStu.getScore())
#newStu.setScore(151)
print(newStu.getScore())
#newStu.setScore(-150)
print(newStu.getScore())

#改造Student对象的封装，使用@property
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an Integer')
        if value < 0 or value >150:
            raise ValueError('Score must be 0 ~ 150')
        self._score = value

newStuOne = Student()
newStuOne.score = 150
print(newStuOne.score)
#newStuOne.score = 151
print(newStuOne.score)
#newStuOne.score = -151
print(newStuOne.score)

#定义只读属性(只有getter方法，没有setter方法)
class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self.birth = value

    @property
    def age(self):
        return 2015 - self._birth

#小练习：请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('Width must be an Integer')
        if value < 0:
            raise ValueError('Width must be greater than 0')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('Height must be an Integer')
        if value < 0:
            raise ValueError('Height must be greater than 0')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution

#多重继承
class Animal:
    pass

#大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

#各种动物
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

#功能类
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying')

#多重继承
class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

#MixIn实例
# class MyTCPServer(TCPServer, ForkingMixIn):
#     pass
#
# class MyUDPServer(UDPServer, ThreadingMixIn):
#     pass
#
# class MyTCPServer(TCPServer, CoroutineMixIn):
#     pass
#定制类
#定义一个类，打印实例
class Student(object):
    def __init__(self, name):
        self.name = name

print(Student('Sunshine'))
#__str__()方法的使用
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student Object (name : %s)' % self.name
print(Student('Sunshine'))

stuThree = Student('Sunshine')
print(stuThree)

#__repr__()方法的使用，__repr__()与__str__()代码相同，代码可以这样写
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student Object (name : %s)' % self.name
    __repr__ = __str__
print(Student('Sunshine'))

#斐波那契数列
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            return StopIteration()
        return self.a
# for n in Fib():
#     print(n)

# print(Fib()[5])

#__getitem__()方法
class Fib(object):
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a,  b = b, a + b
        return a

print(Fib()[10])

#可以传入int和切片的__getitem__()方法
class Fib(object):
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
        elif isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
f = Fib()
print(f[0:5])
print(f[:20])

#__getattr__()方法的使用
class Student(object):
    def __init__(self, name):
        self.name = name
stuFour = Student('Sunshine')
print(stuFour.name)
# print(stuFour.score)

class Student(object):
    def __init__(self, name):
        self.name = name
    def __getattr__(self, item):
        if item == 'score':
            return 99
stuFive = Student('Sunshine')
print(stuFive.name)
print(stuFive.score)

#__getattr__()方法返回函数
class Student(object):
    def __getattr__(self, item):
        if item == 'score':
            return lambda: 150
stuSix = Student()
print(stuSix.score())
#更完善的__getattr__方法
class Student(object):
    def __getattr__(self, item):
        if item == 'score':
            return lambda : 150
        return AttributeError('\'Student\' Object has no attribute \'%s\'' % item)
stuSeven = Student()
print(stuSeven.score())
print(stuSeven.age)

#链式调用
class Chain(object):
    def __init__(self, path=''):
        self.path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self.path, path))
    def __str__(self):
        return self.path
    __repr__ = __str__
print(Chain().status.user.timeline.list)

#__call__()方法的使用
class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s.' % self.name)
stuEight = Student('Sunshine')
print(stuEight())

#判断一个对象能否被调用
print(callable(Student('Sunshine')))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('Sunshine'))