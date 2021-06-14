from lib.crypto import AESCipher
import sys

db = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'port': 3306,
    'database': 'swith'
}
DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"


class Config(object):
    VERSION = 0.1
    JWT_SECRET_KEY = sys.argv[1]
    CIPHER = AESCipher(sys.argv[1])

    @staticmethod
    def decrypt(str_data):
        return Config.CIPHER.decrypt(str_data)


class DevelopmentConfig(Config):
    HOST = '0.0.0.0'
    PORT = 5000
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    HOST = '0.0.0.0'
    PORT = 5000
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
