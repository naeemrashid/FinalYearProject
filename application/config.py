import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True
MONGO_HOST = 'localhost'
MONGO_PORT='27017'
MONGO_DBNAME='app_db'