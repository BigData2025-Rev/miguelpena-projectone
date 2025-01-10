from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from api.schemas.balance import BalanceSchema
from extensions import db
from auth.decorators import auth_role
from models.balances import Balance

class BalanceList(Resource):
    method_decorators = [auth_role('admin'), jwt_required()]
    def get(self):
        balances = Balance.query.all() #equivalent to running SELECT * FROM balance;
        schema = BalanceSchema(many=True)
        return {'results': schema.dump(balances)}
    
    method_decorators = [auth_role('user'), jwt_required()]
    def post(self):
        schema = BalanceSchema()
        validated_data = schema.load(request.json)
        balance = Balance(**validated_data)

        db.session.add(balance)
        db.session.commit() #adds ACID properties to SQL database.

        return {'msg':'Balance Created', 'balance':schema.dump(balance)}

    
class BalanceResource(Resource):
    method_decorators = [auth_role(['user', 'admin']), jwt_required()]
    def get(self, account_id):
        balance = Balance.query.filter_by(account_id=account_id).first() #equivalent to SELECT * FROM accounts WHERE accounts.username=? LIMIT 1; where ? is usually replaced with username in Spring.
        if balance is None:
            return {'msg':'This account does not have a balance!'}
        
        schema = BalanceSchema()

        return {'account': schema.dump(balance)}
    
    method_decorators = [auth_role('user'), jwt_required()]
    def put(self, account_id):
        schema = BalanceSchema(partial=True)
        balance = Balance.query.filter_by(account_id=account_id).first()
        balance = schema.load(request.json, instance=balance)
        # account.password = validated_data.get('password') #the setter for the account object triggers an DML query: UPDATE accounts SET accounts.password=? WHERE accounts.username=?; 
        db.session.add(balance)
        db.session.commit()

        return {'msg':'Balance Updated', 'balance': schema.dump(balance)}
    
    method_decorators = [auth_role('admin'), jwt_required()]
    def delete(self, account_id):
        balance = Balance.query.filter_by(account_id=account_id).first()
        if balance is None:
            return {'msg':'Balance does not exist!'}
        
        db.session.delete(balance) #triggers a DML query: DELETE FROM balances WHERE balances.account_id=?; Typically, NOTE: ondelete='CASCADE' property will maintain referential integrity.
        db.session.commit()

        return {'msg':'Balance Deleted'}