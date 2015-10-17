#/usr/bin/env python
# -*- coding: UTF-8 -*-

from fields.fields import *
from models.model import Model


class User(Model):
	
	id = StringField(column_type='VARCHAR(100)',primary_key=True, default='12345')
	uname = StringField(column_type='VARCHAR(50)')

if __name__ == '__main__':
	u = User(uname='cookie',age=100)
	print (dir(u))
	#print (u.age)
	#User.find(where='email=? AND id=?', args=['cokie@foxmail.com', '123'], orderby='id DESC')
	u.remove()
	