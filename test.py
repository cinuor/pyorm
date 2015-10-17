#/usr/bin/env python
# -*- coding: UTF-8 -*-

import time, uuid

from fields.fields import *
from models.model import Model
from db.dboperation import create_pools


def next_id():
	return '%015d%s000' %(int(time.time()*1000), uuid.uuid4().hex)

class User(Model):
	
	id = StringField(ddl='VARCHAR(50)',primary_key=True, default=next_id())
	name = StringField(ddl='VARCHAR(50)')
	email = StringField(ddl='VARCHAR(50)')

if __name__ == '__main__':
	config = {
		'host':'127.0.0.1',
		'port':3306,
		'user':'root',
		'password':'root',
		'database':'test'
	}
	create_pools(**config)
	l = User.findAll(orderby='name ASC')
	print (l)