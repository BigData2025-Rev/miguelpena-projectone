from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from api.schemas import AdminViewBalanceSchema, BalanceSchema, BalanceCreateSchema
from extensions import db
from auth.decorators import auth_role
from models import Balance

class BalanceList(Resource):
    method_decorators = [auth_role('admin'), jwt_required()]
    def get(self):
        balances = Balance.query.all() #equivalent to running SELECT * FROM balance;
        schema = AdminViewBalanceSchema(many=True)
        return {'results': schema.dump(balances)}
    
    method_decorators = [jwt_required()]
    def post(self):
        account_id = get_jwt_identity()
        schema = BalanceSchema()
        validated_data = schema.load(request.json)

        validated_data['account_id'] = account_id
        
        balance = Balance(**validated_data)

        db.session.add(balance)
        db.session.commit() #adds ACID properties to SQL database.

        return {'msg':'Balance Created', 'balance': schema.dump(balance)}

class BalanceResource(Resource):
    method_decorators = [jwt_required()]
    def get(self):
        account_id = get_jwt_identity()
        balance = Balance.query.filter_by(account_id=account_id).first() #equivalent to SELECT * FROM accounts WHERE accounts.username=? LIMIT 1; where ? is usually replaced with username in Spring.
        if balance is None:
            return {'msg':'This account does not have a balance!'}
        
        schema = BalanceSchema()

        return {'balance': schema.dump(balance)}
    
    method_decorators = [jwt_required()]
    def put(self):
        account_id = get_jwt_identity()
        schema = BalanceSchema(partial=True)
        balance = Balance.query.filter_by(account_id=account_id).first()
        if balance is None:
            return {'msg':'This account does not have a balance!'}, 400
        
        balance = schema.load(request.json, instance=balance)
        # account.password = validated_data.get('password') #the setter for the account object triggers an DML query: UPDATE accounts SET accounts.password=? WHERE accounts.username=?; 
        db.session.add(balance)
        db.session.commit()

        return {'msg':'Balance Updated', 'balance': schema.dump(balance)}