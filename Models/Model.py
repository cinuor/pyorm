#/usr/bin/env python
# -*- coding: UTF-8 -*-

from MetaClasses.ModelMetaClass import ModelMetaClass


class Model(dict,metaclass=ModelMetaClass):
	#__metaclass__ = ModelMetaClass
	def __init__(self, **kwargs):
		super(Model, self).__init__(**kwargs)

		#检查必要参数是否填写
		for k,v in self.__mapping__.items():
			if v.default is None and k not in self:
				raise ValueError("%s field should not be null" %k)
			#不填写id等默认值时，将field中的默认值给dict
			elif v.default is not None and k not in self:
				setattr(self, k, self.__mapping__[k].default)

	#获取到的是dict部分的值
	def __getattr__(self, key):
		try:
			return self[key]
		except Exception as e:
			raise AttributeError('No Such attribute named %s' %key)
		

	def __setattr__(self, key, value):
		self[key] = value

	#获取到的是field
	def getValue(self,key):
		try:
			return getattr(self, key, None)
		except Exception as e:
			raise ValueError('No Such attribute named %s' %key)

	@classmethod
	def find(cls, where=None, args=None, **kw):
		sql = [cls.__select__]
		if where is not None:
			if args is None:
				raise ValueError('args should not be empty')
			if not isinstance(args, list):
				raise ValueError('args should be a list')
			if len(where.split('='))-1 != len(args):
				raise ValueError('args does not match')
			sql.append('WHERE')
			sql.append(where)
		if 'orderby' in kw.keys():
			sql.append('ORDER')
			sql.append('BY')
			sql.append(kw.get('orderby'))

		print (' '.join(sql))
		#do some other things