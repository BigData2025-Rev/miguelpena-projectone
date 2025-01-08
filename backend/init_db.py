"""
    NOTE: Do not run the usual way! 
    Open a powershell, and run the following command:
    flask shell

    which should open a REPL with flask application context present in it.
    copy and paste the following code.

"""

from app import db
from models.accounts import Account

db.create_all()