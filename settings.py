import environ


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

