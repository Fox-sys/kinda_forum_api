import environ
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta


env = environ.Env(
    DEBUG=(bool, True),
    DB_NAME=(str, 'name'),
    DB_USER=(str, 'user'),
    DB_PASS=(str, 'pass'),
    DB_HOST=(str, 'localhost'),
    DB_PORT=(int, 5432),
    COOKIE_LIFE_TIME=(int, 3600),
    SECRET_KEY=(str, 'key')
)

DEBUG = env('DEBUG')
DB_NAME = env('DB_NAME')
DB_USER = env('DB_USER')
DB_PASS = env('DB_PASS')
DB_HOST = env('DB_HOST')
DB_PORT = env('DB_PORT')
COOKIE_LIFE_TIME = env('COOKIE_LIFE_TIME')
SECRET_KEY = env('SECRET_KEY')

DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
Base: DeclarativeMeta = declarative_base()
