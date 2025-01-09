from flask import request, jsonify
from flask_restful import Resource, abort
from flask_jwt_extended import jwt_required

from api.schemas.account import AccountSchema
from extensions import db
from models.accounts import Account

class AccountList(Resource):
    method_decorators = [jwt_required()]
    def get(self):
        accounts = Account.query.all() #equivalent to running SELECT * FROM accounts;
        schema = AccountSchema(many=True)
        return {'results': schema.dump(accounts)}
    
    # def post(self):
    #     schema = AccountSchema()
    #     validated_data = schema.load(request.json)
    #     #validation of data will mostly occur in the frontend for now, but I can add an additional layer of security with FLask-Marshmellow
    #     account = Account(**validated_data)

    #     db.session.add(account)
    #     db.session.commit() #adds ACID properties to SQL database.

    #     return {'msg':'Account Created', 'account':schema.dump(account)}
    
# class AccountResource(Resource):
#     def get(self, username):
#         account = Account.query.filter_by(username=username).first() #equivalent to SELECT * FROM accounts WHERE accounts.username=? LIMIT 1; where ? is usually replaced with username in Spring.
#         if account is None:
#             return {'msg':'Account does not exist!'}
        
#         schema = AccountSchema()

#         return {'account': schema.dump(account)}
    
#     def put(self, username):
#         schema = AccountSchema(partial=True)
#         account = Account.query.filter_by(username=username).first()
#         account = schema.load(request.json, instance=account)
#         # account.password = validated_data.get('password') #the setter for the account object triggers an DML query: UPDATE accounts SET accounts.password=? WHERE accounts.username=?; 
#         db.session.add(account)
#         db.session.commit()

#         return {'msg':'Account Updated', 'account': schema.dump(account)}
    
#     def delete(self, username):
#         account = Account.query.filter_by(username=username).first()
#         if account is None:
#             return {'msg':'Account does not exist!'}
        
#         db.session.delete(account) #triggers a DML query: DELETE FROM accounts WHERE accounts.username=?; Typically, NOTE: ondelete='CASCADE' property will maintain referential integrity.
#         db.session.commit()

#         return {'msg':'Account Deleted'}

