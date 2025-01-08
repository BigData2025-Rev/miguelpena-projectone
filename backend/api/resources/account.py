from flask import request, jsonify
from flask_restful import Resource, abort

from extensions import db
from models.accounts import Account

class AccountList(Resource):
    def get(self):
        accounts = Account.query.all() #equivalent to running SELECT * FROM accounts;
        return jsonify(results=accounts)
    
    def post(self):
        data = request.json
        #validation of data will mostly occur in the frontend for now, but I can add an additional layer of security with FLask-Marshmellow
        account = Account(
            username=data.get('username'),
            password=data.get('password')
        )

        db.session.add(account)
        db.session.commit() #adds ACID properties to SQL database.

        return jsonify(msg='Account Created', account=account)
    
class AccountResource(Resource):
    def get(self, account_id):
        account = Account.query.get_or_404(account_id) #equivalent to SELECT * FROM accounts WHERE accounts.id=?; where ? is usually replaced with account_id in Spring.

        return jsonify(account=account)
    
    def put(self, account_id):
        data = request.json

        account = Account.query.get_or_404(account_id)
        account.password = data.get('password') #the setter for the account object triggers an DML query: UPDATE accounts SET accounts.password=? WHERE accounts.id=?; 

        db.session.commit()

        return jsonify(msg='Account Updated', account=account)
    
    def delete(self, account_id):
        account = Account.query.get_or_404(account_id)

        db.session.delete(account) #triggers a DML query: DELETE FROM accounts WHERE accounts.id=?; Typically, NOTE: ondelete='CASCADE' property will maintain referential integrity.
        db.session.commit()

        return jsonify(msg='Account Deleted')

