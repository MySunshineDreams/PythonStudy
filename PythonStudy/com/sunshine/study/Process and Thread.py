#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Process and Thread'

#多进程与多线程

#创建子进程
import os

print('Process (%s) starts...' % os.getpid())

#Only Works On Unix/Linux/Mac
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s' % (os.getpid(), os.getppid()))
# else:
#     print('I am parent process (%s) and create a child process %s' % (os.getpid(), pid))

#multiprocessing创建子进程
from multiprocessing import Process
import os

#子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('Child Process will start...')
    p.start()
    p.join()
    print('Child Process ends...')

#进程池创建子进程
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds' % (name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocess done...')
    p.close()
    p.join()
    print('All sub process done.')

#Python中运行nslookup www.python.org
import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code', r)

#communicate()方法追加指令
import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('GBK'))
print('Exit code', p.returncode)

#进程间通信
#创建两个子进程，一个往Queue里写数据，一个从Queue里读取数据
from multiprocessing import Process, Queue
import os, time, random

#写数据执行的代码
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

#读取数据执行代码
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

#主函数
if __name__ == '__main__':
    #父进程创建Queue，并传给各子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    #启动子线程pw写入
    pw.start()
    #启动子进程pr，读取
    pr.start()
    #等待pw结束
    pw.join()
    #pr进程是死循环，无法等待其结束，只能强行终止
    pr.terminate()

#多线程
#创建并启用一个线程
import time, threading

def loop():
    print('Thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('Thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('Thread %s ended' % threading.current_thread().name)

print('Thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('Thread %s ended' % threading.current_thread().name)

#没有锁的多线程会改乱数据
import time, threading

#假设这是你的银行存款
#这个例子有点像脏读
balance = 0

def change_it(n):
    #先存后取，存款为0
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(9,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

#同步锁
balance

#声明锁
lock = threading.Lock()

def run_thread(n):
    for i in range(1000000):
        #获取锁
        lock.acquire()
        try:
            #放心的修改
            change_it(n)
        finally:
            #使用锁之后，释放锁
            lock.release()

#Python写个死循环
# import  threading, multiprocessing
#
# def loop():
#     x = 0
#     while True:
#         x = x + 1
#
# for i in range(multiprocessing.cpu_count()):
#     t1 = threading.Thread(target=loop)
#     t2 = threading.Thread(target=loop)
#     t1.start()
#     t2.start()

#ThreadLocal的用法
import threading

#创建全局的ThreadLocal对象
local_student = threading.local()

class Student(object):
    def __init__(self, name):
        self.name = name

def process_student():
    #获取当前线程关联的student
    stuOne = local_student.student
    print('Hello, %s (in %s)' % (stuOne, threading.current_thread().name))

def process_thread(name):
    #绑定ThreadLocal的student
    local_student.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Sunshine',), name='Sunshine')
t2 = threading.Thread(target=process_thread, args=('Sundial丶Dreams',), name='Sundial丶Dreams')
t1.start()
t2.start()
t1.join()
t2.join()

import random, time, queue
from multiprocessing.managers import BaseManager

#发送任务的队列
task_queue = queue.Queue()

#接收任务的队列
receive_queue = queue.Queue()

#从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

#把两个Queue都注册到网络上，callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable=lambda : task_queue)
QueueManager.register('get_receive_queue', callable=lambda : receive_queue)

#绑定端口5000，验证码是"abc"
manager = Queue(address=('', 5000), authkey=b'abc')

#启动Queue
manager.start()

#获取通过网络访问的Queue对象
task = manager.get_task_queue()
receive = manager.get_receive_queue()

#放几个任务进去
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)

#从receive队列读取结果
print('Try get receive...')
for i in range(10):
    r = receive.get(timeout=10)
    print('Result:%s' % r)

#关闭
manager.shutdown()
print('Manager exit.')

