import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'test-recipe-service')
    DATABASE_USER = os.environ.get('DATABASE_USER', 'admin')
    DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'admin')
    PSQL_SERVER = os.environ.get('PSQL_SERVER', 'localhost')
    URL_DB = os.environ.get('URL_DB', f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}')
    ALGORITHM = os.environ.get('ALGORITHM', "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES', 30)
    BASE_DIR_IMAGES = os.environ.get('BASE_DIR_IMAGES', '/usr/src/images')
