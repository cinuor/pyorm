#/usr/bin/env python
# -*- coding: UTF-8 -*-

from mysql.connector.pooling import MySQLConnectionPool
from error import ConnectionError

global _pool

# global conn

# def connect(host, port, database, user, password):
# 	global conn
# 	try:
# 		conn = mysql.connector.connect(user=user, password=password, database=database, host=host, port=port, use_unicode=True)
# 	except Exception as e:
# 		raise e

config = {
	'host':'127.0.0.1',
	'port':3306,
	'database':'test',
	'user':'root',
	'password':'root'
}

#create connection pools
def create_pools(pool_size=5, **kw):
	global _pool
	try:
		_pool = MySQLConnectionPool(pool_size, **kw)
	except Exception as e:
		raise e
#get a connection from the connection pool
def get_connection():
	global _pool
	if _pool is None:
		raise ConnectionError('No connections')
	try:
		conn = _pool.get_connection()
		return conn
	except Exception as e:
		raise e

#select operation
def select(sql, args, size=None):
	sql.replace('?', '%s')
	conn = get_connection()
	try:
		cur = conn.cursor()
		cur.execute(sql, args or ())
		if size:
			rs = cur.fetchmany(size)
		else:
			rs = cur.fetchall()
		cur.close()
		conn.close() #put the connection into the queue, not realsing the connection
		return rs
	except Exception as e:
		raise e

def execute(sql, args, autocommit=True):
	sql.replace('?', '%s')
	conn = get_connection()
	try:
		cur = conn.cursor()
		cur.execute(sql, args)
		affected = cur.rowcount
		cur.close()
		conn.close() #put the connection into the queue, not realsing the connection
		if not autocommit:
			conn.commit()
	except Exception as e:
		if not autocommit:
			conn.rollback()
		raise e



