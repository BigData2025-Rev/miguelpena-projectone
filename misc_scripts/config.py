import os

from dotenv import load_dotenv

load_dotenv('./.env')

MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASS = os.environ.get('MYSQL_PASS')
MONGODB_CLIENT = os.environ.get('MONGODB_CLIENT')