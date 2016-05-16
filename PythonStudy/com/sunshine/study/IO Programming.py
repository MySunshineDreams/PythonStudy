#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'IO编程'

#IO编程

#使用Python内建的open()打开一个文件对象
f = open('PythonSix.py', 'rb')
print(f.read())

#关闭读取文件对象
f.close()

#比较完整的文件读取代码
try:
    f = open('PythonSix.py', 'rb')
    print(f.read())
except:
    raise IOError('Reading File Error!')
finally:
    if f:
        f.close()

#Python的with语句自动调用close()方法
with open('PythonSix.py', 'rb') as f:
    print(f.read())

#readlines()用法
f = open('PythonSix.py', 'rb')
for line in f.readlines():
    print(line.strip()) #把末尾的"\n删掉"

#StringIO
#创建一个StringIO
from io import StringIO
f = StringIO()
print(f.write('Hello'))
print(f.write(', '))
print(f.write('Sunshine'))
print(f.getvalue())

#读取StringIO的值
from io import StringIO
f = StringIO('Hello\nSunshine')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

#BytesIO用法
from io import BytesIO
f = BytesIO()
print(f.write('暖阳'.encode('UTF-8')))
print(f.getvalue())

#读取BytesIO
from io import BytesIO
f = BytesIO(b'\xe6\x9a\x96\xe9\x98\xb3')
print(f.read())

#操作文件和目录
import os
print(os.name)
# print(os.uname())

#环境变量
print(os.environ)

print(os.environ.get('PYTHON_HOME'))
print(os.environ.get('python_home'))

#操作文件和目录(函数一部分放在os模块中，一部分放在os.path模块中)
#查看当前目录的绝对路径
print(os.path.abspath('.'))
#在某个目录下创建一个新目录，首先把新目录完整路径表示出来
print(os.path.join(os.path.abspath('.'), 'testDir'))
#然后创建一个目录
print(os.mkdir(os.path.join(os.path.abspath('.'), 'testDir')))
#然后删除目录
print(os.rmdir(os.path.join(os.path.abspath('.'), 'testDir')))
#拆分路径
print(os.path.split(os.path.abspath('.')))
#os.path.splitext()方法获取文件扩展名
print(os.path.splitext('IO Programming.py'))
#假设当前目录下有text.txt文件，进行操作文件和目录
#重命名
# print(os.rename('text.txt', 'text.py'))
#删除
# print(os.remove('text.py'))
#列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
#列出所有的.py文件
print([x for x in os.listdir('.') if os.path.isdir(x) and os.path.splitext(x)[1] == 'py'])

#序列化
#定义一个dict
dictOne = dict(name='Sunshine', score=150, sex='male')

#将一个对象序列化并写入文件
import pickle
dictOne = dict(name='Sunshine', score=150, sex='male')
print(pickle.dumps(dictOne))

f = open('dump.txt', 'wb')
pickle.dump(dictOne, f)
f.close();

f = open('dump.txt', 'rb')
dictOne = pickle.load(f)
f.close()
print(dictOne)

#Python内置模块：JSON
#Python对象编程JSON
import json
dictTwo = dict(name='Sunshine', sex='male', score=150)
print(json.dumps(dictTwo))

#JSON的反序列化
jsonStr = '{"sex": "male", "score": 150, "name": "Sunshine"}'
print(json.loads(jsonStr))
print(isinstance(json.loads(jsonStr), dict))

#序列化class对象
import json
class Student(object):
    def __init__(self, name, sex, score):
        self.name = name
        self.sex = sex
        self.score = score

stuOne = Student('Sunshine', 'male', '150')
# print(json.dumps(stuOne))

#转换函数
def student2dict(student):
    return {
        'name' : student.name,
        'sex' : student.sex,
        'score' : student.score
    }

print(json.dumps(stuOne, default=student2dict))

#JSON转换为实例对象
jsonStrTwo = '{"name": "Sunshine", "sex": "male", "score": "150"}'
def dict2instance(d):
    return Student(d['name'], d['sex'], d['score'])

print(json.loads(jsonStrTwo, object_hook=dict2instance))