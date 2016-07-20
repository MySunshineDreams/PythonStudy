#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'连接MySQL'

# 连接MySQL

# 导入MySQL驱动
import mysql.connector
# 建立链接
conn = mysql.connector.connect(user='root', password='yangsl', database='test')
cursor = conn.cursor()
# 创建User表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一条记录，注意MySQL的占位符是%s
cursor.execute('insert into user (id, name) values(%s, %s)', ['1', 'Sunshine'])
cursor.rowcount
# 提交事务
conn.commit()
cursor.close()
# 运行查询
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ['1'])
value = cursor.fetchall()
print(value)
# 关闭Cursor和Connection
cursor.close()
conn.close()

# SQLAlchemy的实现
# 第一步：SQLAlchemy
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义User对象
class User(Base):
	# 表的名字
	__tablename__ = 'user'

	# 表的结构
	id = Column(String(20), primary_key=True)
	name = Column(String(20))

# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:password@127.0.0.1:3306/test')

# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 加入School表
class School(Base):
	__tablename__ = 'School'
	id = Column(String(20), primary_key=true)
	name = Column(String(20))

# 创建session对象
session = DBSession()
# 创建User对象
new_user = User(id='1', name='sunshine')
# 添加到session
session.add(new_user)
# 提交保存到数据库
session.commit()
# 关闭session
session.close()

# 使用SQLAlchemy从数据库中查出数据
# 创建session
sessionTwo = DBSession()
# 用all()则返回所有行
# 创建Query查询，filter是where条件，最后调用one()返回唯一一行，如果调
user = session.query(User).filter(User.id=='1').one()
# 打印类型和对象的name属性
print('type', type(user))
print('type', user.name)
# 关闭session
session.close()

# SQLAlchemy的一对多关系
class User(Base):
	__tablename__ = 'user'

	id = Column(String(20), primary_key=true)
	name = Column(String(20))

	#一对多
	books = relationship('Book')

class Book(Base):
	__tablename__ = 'book'

	id = Column(String(20), primary_key=true)
	name = Column(String(20))

	# "多"的一方的book表示通过外键关联到User表的
	user_id = Column(String(20), ForeignKey('user.id'))
