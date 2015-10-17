#/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
from mysql.connector.pooling import MySQLConnectionPool

global _pool

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
	conn = get_connection()
	try:
		cur = conn.cursor(dictionary=True)
		cur.execute(sql.replace('?', '%s'), args or ())
		if size:
			rs = cur.fetchmany(size)
		else:
			rs = cur.fetchall()
		cur.close()
		conn.close() #put the connection into the queue, not realsing the connection
		return rs
	except Exception as e:
		raise e

def execute(sql, args):
	conn = get_connection()
	try:
		cur = conn.cursor()
		logging.info(sql.replace('?', '%s'))
		cur.execute(sql.replace('?', '%s'), args)
		affected = cur.rowcount
		print (affected)
		if affected == 1:
			conn.commit()
		else:
			conn.rollback()
		cur.close()
		conn.close() #put the connection into the queue, not realsing the connection
		return affected
	except Exception as e:
		conn.rollback()
		raise e

class BaseError(Exception):
	def __init__(self, error, message):
		super(baseError, self).__init__(message)
		self.error = error
		self.message = message

class ConnectionError(BaseError):
	def __init__(self, message):
		super(ConnectionError, self).__init__('Connection Error', message)

