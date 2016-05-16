#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'异步IO'

# 异步IO

# asynio实现hello world
# import asyncio
#
# @asyncio.coroutine
# def hello():
# 	print('hello world')
# 	# 异步调用asynio.sleep(1)
# 	r = yield from asyncio.sleep(1)
# 	print('hello world')
#
# # 获取EventLoop
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

# Task封装两个coroutine
import threading
import asyncio

# @asyncio.coroutine
# def hello():
# 	print('hello world! (%s)' % threading.currentThread())
# 	yield from asyncio.sleep(1)
# 	print('hello world! (%s)' % threading.currentThread())
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# 使用asyncio异步网络连接sina、sohu和163的网站首页
import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHOST: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(tasks)
loop.close()

# 编写http服务器，处理url
import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Responese(body=b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.01', 8000)
    print('Server started at http://127.0.01:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

do_somecode()
f = open('/path/to/file', 'r')
r = f.read() # 线程在此处等待IO结果
# IO操作完成后才能继续执行
do_somecode(r)

# 异步IO处理过程介绍
loop = get_event_loop()
while True:
	event = lopp.get_event()
	process_event(event)

# 协程：生产者-消费者
def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return 
		print('[CONSUMER] Consuming %s...' % n)
		r = '200 ok'

def produce(c):
	c.send(None)
	n = 0
	while n < 5:
		n = n + 1
		print('[PRODUCER] Producing %s...' % n)
		r = c.send(n)
		print('[PRODUCER] Consumer return:%s' % n)
	c.close()

c = consumer()
produce(c)
