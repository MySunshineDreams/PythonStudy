#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'面向对象编程'

#面向对象编程

#面向过程处理学生成绩表
dictOne = {'name' : 'Yang', 'score' : '150'}
dictTwo = {'name' : 'Wang', 'score' : '89'}

#面向过程打印学生成绩
def funcOne(dict):
    print('%s: %s' % (dict['name'], dict['score']))
funcOne(dictOne)
funcOne(dictTwo)

#面向对象处理学生成绩表
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s : %s' % (self.name, self.score))
studentOne = Student('Yang', '150')
studentTwo = Student('Wang', '89')
studentOne.print_score()
studentTwo.print_score()

studentOne.name = 'YangSL'
print(studentOne.name)

#通过函数打印学生成绩
def print_score(student):
    print('%s %s' % (student.name, student.score))
print_score(studentOne)
def funcOne(dict):
    print('%s: %s' % (dict['name'], dict['score']))

#封装可以给类增加新的方法
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s : %s' % (self.name, self.score))
    def get_grade(self):
        if int(self.score) >= 130:
            return '优秀'
        elif int(self.score) >= 90:
            return '及格'
        else:
            return '不及格'
studentOne = Student('Yang', '150')
print(studentOne.get_grade())

#类中私有属性
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s %s' % (self.name, self.score))
studentOne = Student('Yang', '150')

#类声明getter方法
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s %s' % (self.name, self.score))

    def get_name(self):
        return self.__name

    def get_grade(self):
        return self.__score
studentOne = Student('Yang', '150')
print('学生', studentOne.get_name(), '分数是', studentOne.get_grade())

#类的getter、setter私有封装
class Student(object):

    def print_score(self):
        print('%s %s' % (self.name, self.score))

    def get_name(self):
        return self.__name

    def get_grade(self):
        return self.__score

    def set_name(self, name):
        self.__name = name
    def set_score(self, score):
        if 0 <= score <= 150:
            self.__score = score
        else:
            raise ValueError('Invalid Score')
studentOne = Student()
studentOne.set_name('杨松霖')
studentOne.set_score(150)
print('学生', studentOne.get_name(), '分数是', studentOne.get_grade())

#__name可以通过_Student__name来获取
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s %s' % (self.name, self.score))
studentOne = Student('杨松霖', 150)
print('学生', studentOne._Student__name, '分数是', studentOne._Student__score)

#继承
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()

dog.run()
cat.run()

class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating bone...')

#对子类进行改进，使其符合自身特性
class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog = Dog()
cat = Cat()

dog.run()
cat.run()

#继承类型判断
print(isinstance(dog, Animal))

a = Animal()
print(isinstance(a, Dog))

#继续理解多态
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

#继续派生Animal
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())

#typpe()判断对象类型
print(type(123))
print(type('Sunshine'))
print(type(None))

print(type(abs))
print(type(a))

#比较两个type类型是否相等
print(type(123) == type(456))
print(type('Sunshine') == type('Yangsl'))
print(type('Sunshine') == str)
print(type('Sunshine') == type(666))

#使用isinstance()判断类型
a = Animal()
dog = Dog()

print(isinstance(a, Animal))
print(isinstance(dog, Animal))

#isinstance()可以判断type()能判断的类型
print(isinstance(123, int))
print(isinstance('Sunshine', str))
print(isinstance(b'a', bytes))

#isinstance()可以判断类型之一
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

#dir()获取所有方法
print(dir('Sunshine'))

#函数调用与属性方法的通用
print(len('Sunshine'))
print('Sunshine'.__len__())

#自定义__len__()
class MyDog(object):
    def __len__(self):
        return 100
myDog = MyDog()
print(len(myDog))

#自带的lower()方法，将字符串所有字符变成小写
print('SUNSHINE'.lower())

#通过getattr()、setattr()和hasattr()操作对象状态
class MyObject(object):
    def __init__(self):
        self.x = 90
    def power(self):
        return self.x * self.x
myObject = MyObject()

print(hasattr(myObject, 'x'))
print(myObject.x)

print(hasattr(myObject, 'y'))
setattr(myObject, 'y', '150')

print(hasattr(myObject, 'y'))
print(getattr(myObject, 'y'))
print(myObject.y)

#如果试图获取不存在的属性，会抛出错误
#print(getattr(myObject, 'z'))

#获取属性时，代入默认值
print(getattr(myObject, 'Sunshine', '150'))

#getattr()、setattr()和hasattr()可以获得对象的方法
hasattr(myObject, 'power')
getattr(myObject, 'power')
fn = getattr(myObject, 'power')
print(fn())

#getattr()、setattr()和hasattr()正确用法
def readImage(fp):
    if hasattr(fp, 'read'):
        #return readData(fp)
        pass
    return None

#枚举类
from enum import Enum

Month = Enum('Month', ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'))

#用Enum派生自定义类
from enum import Enum, unique

@unique #装饰器可以帮助我们检查保证没有重复值
class Weekday(Enum):
    SUN = 0 #SUN的value被设定为0
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
dayOne = Weekday.MON
print(dayOne)
print(Weekday.TUE)
print(Weekday['TUE'])
print(Weekday.TUE.value)
print(dayOne == Weekday.MON)
print(dayOne == Weekday.TUE)
print(Weekday(1))
print(dayOne == Weekday(1))
# print(Weekday(7))

#元类
#定义一个Hello的class
class Hello(object):
    def sayHello(self, name = 'world'):
        print('Hello, %s' % name)

#使用type()方法创建一个Hello子类
def fn(self, name = 'World'):   #先定义函数
    print('Hello, %s' % name)

Hello = type('Hello', (object,), dict(hello = fn))  #创建Hello class
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

#metaclass是类的模板，所以必须从"type"类派生
class ListMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value : self.append(value)
        return type.__new__(cls, name, bases, attrs)

#定义类的时候指定metaclass
class MyList(list, metaclass  = ListMetaClass):
    pass

L = MyList()
L.add(1)
print(L)

LOne = list()
LOne.add(1)