import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
class BaseConfig():
    DEBUG = True
    MONGO_HOST = '127.0.0.1'
    MONGO_PORT='27017'
    MONGO_DBNAME='app_db'
    SECRET_KEY = '6EF6B30F9E557F948C402C89002C7C8A'
class TestConfig(BaseConfig):
    MONGO_DBNAME='test_db'