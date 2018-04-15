import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True
MONGO_HOST = '127.0.0.1'
MONGO_PORT='27017'
MONGO_DBNAME='app_db'
SECRET_KEY = 'Put your secret key here'