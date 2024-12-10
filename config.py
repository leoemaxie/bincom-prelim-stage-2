import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'mysql+pymysql://username:password@localhost/bincomphptest'
    SQLALCHEMY_TRACK_MODIFICATIONS = False