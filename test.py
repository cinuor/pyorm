#/usr/bin/env python
# -*- coding: UTF-8 -*-

from Fields.fields import *
from Models.Model import Model


class User(Model):
	
	id = StringField(column_type='VARCHAR(100)',primary_key=True, default='12345')
	uname = StringField(column_type='VARCHAR(50)')
	age = IntegerField()

if __name__ == '__main__':
	u = User(uname='cookie',age=100)
	print (dir(u))
	print (u.age)