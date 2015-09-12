import os

SECRET_KEY = 'you-will-never-guess'
DEBUG=True
DB_USERNAME = 'fromzeroedu'
DB_PASSWORD = '' # not required for cloud9
BLOG_DATABASE_NAME = 'blog'
DB_HOST = os.getenv('IP', '0.0.0.0')
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI