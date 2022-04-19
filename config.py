import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = "mysql_link"
    SQLALCHEMY_DB_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False