import os
from dotenv import load_dotenv

load_dotenv('./.env')

FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT', 9000)
