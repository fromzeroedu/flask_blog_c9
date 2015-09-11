import os

SECRET_KEY = 'you-will-never-guess'
DEBUG=True
DB_USER = 'fromzeroedu'
DB_PASSWORD = '' # not required for cloud9
DB_DATABASE = 'blog'
DB_HOST = os.getenv('IP', '0.0.0.0')
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USER, DB_PASSWORD, DB_HOST, DB_DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
