#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'内建模块'

#内建模块

from datetime import datetime

now = datetime.now()
print(now)
print(type(now))

#指定某个日期和时间
from datetime import datetime

dt = datetime(2016, 1, 15, 12, 30)
print(dt)
dt = datetime(2016, 1, 15, 12, 30, 30, 23)
print(dt)

#datetime转换为timestamp
from datetime import datetime
dt = datetime(2016, 1, 15, 12, 30)
print(dt.timestamp())
dt = datetime(2016, 1, 15, 12, 30, 30, 23)
print(dt.timestamp())

#timestamp转换成datetime
from datetime import datetime
tsOne = 1452832200.0
tsTwo = 1452832230.000023
print(datetime.fromtimestamp(tsOne))
print(datetime.fromtimestamp(tsTwo))

#timestamp转换成UTC标准时区的时间
from datetime import datetime
tsThree = datetime.now().timestamp()
print(tsThree)
print(datetime.fromtimestamp(tsThree))
print(datetime.utcfromtimestamp(tsThree))

#str转换为datetime
from datetime import datetime
cday = datetime.strptime('2016-01-14 17:27:35', '%Y-%m-%d %H:%M:%S')
print(cday)

#datetime转换为str
from datetime import datetime
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

#datetime加减
#timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
from datetime import datetime, timedelta
now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

#本地时间转换为UTC时间
from datetime import datetime, timedelta, timezone
#创建utc+8:00时区
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
print(now)
dtFour = now.replace(tzinfo=tz_utc_8)
print(dtFour)

#时区转换
#拿到UTC时间，并强制设置时区为UTC+0:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
#astimezone()将转换时区为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
#astimezone()将北京时间转换为东京时间
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)

#collections集合
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

#验证创建的Point对象是tuple的子类
print(isinstance(p, Point))
print(isinstance(p, tuple))

#namedtuple("名称", [属性list])：
Circle = namedtuple('Circle', ['x', 'y', 'z'])

#deque(双向列表)
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

#defaultdict
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

#OrderedDict
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys()))

#Counter计数器
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)

#Base64的编解码
import base64
print(base64.b64encode(b'Sunshine'))
print(base64.b64decode(b'U3Vuc2hpbmU='))

#"url safe"的base64编码
import base64

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode(b'abcd++//'))

#练习
#请写一个能处理去掉=的base64解码函数
import base64

def safe_base64_decode(s):
    pass

#struct
#32位无符号整数变成字节
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = (n & 0xff)
bs = bytes([b1, b2, b3, b4])
print(bs)

#struct的pack函数把任意数据类型变成bytes
import struct

print(struct.pack('>I', 10240099))

#unpack把bytes变成相应的数据类型
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

print(struct.unpack('<ccIIIIIIHH', b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'))

#hashlib
#计算出一个字符串的MD5值
import hashlib

md5 = hashlib.md5()
md5.update('How to use md5 in python hashlib?'.encode('UTF-8'))
print(md5.hexdigest())

#数据量过大，可以分块调用update()，结果是一样的
import hashlib

md5 = hashlib.md5()
md5.update('How to use md5 '.encode('utf-8'))
md5.update('in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

#改动一个字母后，MD5的值发生了改变
import hashlib

md5 = hashlib.md5()
md5.update('How to use md5 '.encode('utf-8'))
md5.update('in python hashlib'.encode('utf-8'))
print(md5.hexdigest())

#SHA1摘要算法
import hashlib

sha1 = hashlib.sha1()
sha1.update('How to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

#无限迭代器
import itertools

# natuals = itertools.count(1)
# for n in natuals:
#     print(n)

#cycle()迭代器
import itertools

# cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)

import itertools

csTwo = itertools.repeat('Sunshine', 2)
for element in csTwo:
    print(element)

#takewhile()截取一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x : x < 10, natuals)
print(list(ns))

#chain() 一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('My', '丶', 'Sunshine'):
    print(c)

#groupby() 将相邻的重复挑出来放在一起
for key, group in itertools.groupby('SSuunnsshhiinnee'):
    print(key, list(group))

#忽略大小写分组
for key, group in itertools.groupby('SsUuNnSsHhIiNnEe', lambda x : x.upper()):
    print(key, list(group))

#XML解析
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attr):
        print('sax : start_element: %s, attrs: %s' % (name, attr))

    def end_element(self, name):
        print('sax : end_element: %s' % name)

    def char_data(self, text):
        print('sax : char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

#小练习
# 请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取当天和第二天的天气：
# http://weather.yahooapis.com/forecastrss?u=c&w=2151330
# 参数w是城市代码，要查询某个城市代码，可以在weather.yahoo.com搜索城市，浏览器地址栏的URL就包含城市代码。

# HTMLParser
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('<%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%S:' % name)

    def handle_charref(self, name):
        print('&#%s:' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

#urllib
#对豆瓣的一个url进行抓取，返回响应
from urllib import request

with request.urlopen('http://book.douban.com/subject/1770782/') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s : %s' % (k, v))
    # print('Data:', data.decode('UTF-8'))

#模拟iPhone 6请求豆瓣首页
from urllib import request

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s, %s' % (k, v))

# 模拟微博登录
from urllib import request, parse

print('Login to weibo.cn')
telephone = input('Telephone:')
password = input('Password')

login_data = parse.urlencode([
    ('username', telephone),
    ('password', password),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('UserAgent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

# 通过Proxy，用Handler来处理复杂的请求

proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass