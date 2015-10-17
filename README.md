# pyorm
This is a simple ORM tool built  with python.

###Introduction
ORM（Object Relational Mapping）looks like a virtual object database.   
Briefly，It contains most database operations    
and you don't have to write SQL statements in every database operation.

###Usage

```Python
import time, uuid

from fields.fields import *
from models.model import Model
from db.dboperation import create_pools

#configuration
config = {
	'host':'127.0.0.1',
	'port':3306,
	'user':'root',
	'password':'root',
	'database':'test'
	}

#generate id
def next_id():
	return '%015d%s000' %(int(time.time()*1000), uuid.uuid4().hex)

#User table in ORM
class User(Model):
	id = StringField(ddl='VARCHAR(50)',primary_key=True, default=next_id())
	name = StringField(ddl='VARCHAR(50)')
	email = StringField(ddl='VARCHAR(50)')

if __name__ == '__main__':
	create_pools(**config)
	user = User(name='Harry Potter', email='harrypotter@Hogwarts.com')
	#insert a user
	user.save()
```

###Dependence
*Python 3.x (take a very small change that you can it on Python 2.x)   
  [Python 3.x](https://www.python.org/downloads/release/python-350/)   

*mysql-connector-python
```shell
pip install mysql-connector-python
```   
or [here to download](http://dev.mysql.com/downloads/connector/python/1.0.html)   


If you think it is a little bit useful,please take a star!   

####Thank you!




