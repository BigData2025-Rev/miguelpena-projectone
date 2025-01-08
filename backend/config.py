import os

from dotenv import load_dotenv

load_dotenv('./.env')

FLASK_DEBUG = os.environ.get('FLASK_DEBUG', False)
FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT', 9000)
FLASK_RUN_HOST = os.environ.get('FLASK_RUN_HOST', "0.0.0.0")
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
MONGODB_CLIENT = os.environ.get('MONGODB_CLIENT')