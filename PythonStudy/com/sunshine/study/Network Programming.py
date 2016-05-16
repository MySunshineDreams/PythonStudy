#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'网络编程'
#网络编程

# 导入Socket库
import socket

# 创建一个sokcet
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
s.connect(('www.sina.com.cn', 80))

# 发送数据
s.send(b'GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据
buffer = []
while True:
	# 每次最多接收1k字节
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)

# 关闭连接
s.close()

# 打印HTTP头
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

# 将网页保存到文件中
with open('sina.html', 'wb') as f:
		f.write(html)

# 简单的服务器程序，用于接收客户端连接
# 把客户端发过来的字符串加上Hello再发送回去
# 创建一个基于IPv4和TCP协议的Socket
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口
s.bind(('127.0.0.1', 9999))

# 调用listen()方法监听端口，参数为最大连接数
s.listen(5)
print('Waiting for connection...')

# 接受来自客户端的连接
while True:
	# 接受一个新连接
	sock, addr = s.accept()
	# 创建新线程来处理TCP连接
	t = threading.Thread(target=tcplink, args=(sock, addr))
	t.start()

# 接受客户端的连接
def tcplink(sock, addr):
	print('Accept new connection from %s:%s' % (sock, addr))
	sock.send(b'Welcome')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('Hello, %s') % data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('Connection from %s:%s is closed' % (sock, addr))

# 客户端
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 9999))
# 接收欢迎消息
print(s.recv(1024).decode('utf-8'))
for data in [b'Micharel', b'Tracy', b'Sarah']:
	# 发送数据
	s.send(data):
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
