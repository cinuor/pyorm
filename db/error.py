#/usr/bin/env python
# -*- coding: UTF-8 -*-

class BaseError(Exception):
	def __init__(self, error, message):
		super(baseError, self).__init__(message)
		self.error = error
		self.message = message

class ConnectionError(BaseError):
	def __init__(self, message):
		super(ConnectionError, self).__init__('Connection Error', message)