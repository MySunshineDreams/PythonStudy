#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'电子邮件'

# 电子邮件

# 构造最简单的纯文本邮件
from email.mime.text import MIMEText
msg = MIMEText('Hello, this is an email', 'plain', 'utf-8')

# 通过SMTP发送邮件
# 输入Email地址和口令
from_addr = input('From:')
password = input('Password:')
# 输入收件人地址
to_addr = input('To:')
# 输入SMTP服务器地址
smtp_server = input('SMTP server:')

import smtplib

# SMTP协议默认端口是25
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

# 发送完整的SMTP协议邮件
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
from email.mime.multipart import  MIMEMultipart

import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr(Header((name, 'utf-8').encode(), addr))

from_addr = input('From:')
password = input('Password:')
to_addr = input('To:')
smtp_server = input('SMTP server:')

msg = MIMEText('Hello, this is an email', 'plain', 'utf-8')
msg['From'] = _format_addr('发件人 <%s>' % from_addr)
msg['To'] = _format_addr('收件人 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候......', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

# 发送附件
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From:'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候......', 'utf-8').encode()

# 邮件正文是MIMEText
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片
with open('D:\File\test.jpg') as f:
		# 设置附件的MIME和文件名，这里是jpg类型。
		mime = MIMEBase('image', 'jpg', filename='test.jpg')
		# 加上必要的头信息
		mime.add_header('Content-Dispostion', 'attachment', filename='test.jpg')
		mime.add_header('Content-ID', '<0>')
		mime.add_header('X-Attachment-Id', '0')
		# 把附件的内容读进来
		mime.set_payload(f.read())
		# 用Base64编码
		encoders.encode_base64(mime)
		# 添加到MIMEMultipart
		msg.attach(mime)

# 发送图片，是把图片放入到HTML代码里
msg.attach(MIMEText('<html><body><h1>Hello</h1><p><img src="cid:0"/></p></body></html>','html', 'utf-8'))

# 同时支持HTML和Plain格式
msg = MIMEMultipart('alternative')
msg['From'] = ...
msg['To'] = ...
msg['Subject'] = ...

msg.attach(MIMEText('Hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))
# 正常发送msg对象

# 加密SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
# 接下来的代码和之前的一样

# 通过POP3协议获取最新的一封邮件的内容
import poplib

# 输入邮件地址，口令和POP3服务器地址
email = input('Email:')
password = input('Password:')
pop3_server = input('POP3 server:')

# 连接到POP3服务器
server = poplib.POP3(pop3_server)
# 可以打开或者关闭调试信息
server.set_debuglevel(1)
# 可选：打印POP3服务器的欢迎文字
print(server.getWelcome().decode('utf-8'))

# 身份认证
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间
print('Message:%s. Size:%s' % server.stat())
# list()返回所有邮件的编号
resp, mails, octets = server.list()
# 可以中查看返回的列表类似[b'1 82923', b'2 2184', ...]
print(mails)

# 获取最新的一封邮件，注意索引号从1开始
index = len(mails)
resp, lines, octets = server.retr(index)

# lines存储了邮件的原始文本的每一行
# 可以获得整个邮件的原始文本
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 稍后解析出邮件
msg = Parser().parsestr(msg_content)

# 可以根据邮件索引号直接从服务器删除邮件
# server.del(index)
# 关闭连接
server.quit()

# 解析邮件
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

import poplib

# 把邮件内容解析为Message对象
msg = Parser().parsestr(msg_content)

# 递归打印出Message的层次结构
# indent用于缩进显示
def print_info(msg, indent = 0):
	if indent == 0:
		for header in ['From', 'To', 'Subject']:
			value = msg.get(header, '')
			if value:
				if header == 'Subject':
					value = decode_str(value)
				else:
					hdr, addr = parseaddr(value)
					name = decode_str(hdr)
					value = u'%s <%s>' % (name, addr)
			print('%s%s:%s' % ('' * indent, header, value))
	if (msg.is_multipart()):
		parts = msg.get_payload()
		for n, part in enumerate(parts):
			print('%spart %s' % (' ' * indent, n))
			print('%s---------' % (' ' * indent))
			print_info(part, indent+1)
	else:
		content_type = msg.get_content_type()
		if content_type == 'text/plain' or content_type == 'text/html':
			content = msg.get_payload(decode=True)
			charset = guess_charset(msg)
			if charset:
				content = content.decode(charset)
			print('%sText:%s' % ('' * indent, content + '...'))
		else:
			print('%sAttachment:%s' % (' ' * indent, content_type))

# 将Subject或者Email中的名字decode
def decode_str(s):
	value, charset = decode_header(s)[0]
	if charset:
		value = value.decode(charset)
	return value

# 检测邮件编码
def guess_charset(msg):
	charset = msg.get_charset()
	if charset is None:
		content_type = msg.get('Content-Type', '').lower()
		pos = content_type.find('charset=')
		if pos >= 0:
			charset = content_type[pos + 8].strip()
	return charset

