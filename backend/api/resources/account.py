from flask import request, jsonify
from flask_restful import Resource, abort
from flask_jwt_extended import jwt_required

from api.schemas import AccountSchema, AccountDetailSchema, AccountRoleSchema, RoleSchema
from extensions import db
from auth.decorators import auth_role
from models import Account, AccountDetail, AccountRole, Role

class AccountList(Resource):
    method_decorators = [auth_role('admin'), jwt_required()]
    def get(self):
        accounts = Account.query.all() #equivalent to running SELECT * FROM accounts;
        schema = AccountSchema(many=True)
        return {'results': schema.dump(accounts)}
    
class AccountDetailList(Resource):
    method_decorators = [jwt_required()]
    def post(self):
        schema = AccountDetailSchema()
        validated_data = schema.load(request.json)
        account_detail = AccountDetail(**validated_data)

        db.session.add(account_detail)
        db.session.commit()

        return {'msg':'Account details were created.', 'account_detail': schema.dump(account_detail)}
    
class AccountDetailResource(Resource):
    method_decorators = [jwt_required()]
    def get(self, account_id):
        account_detail = AccountDetail.query.filter_by(account_id=account_id).first_or_404("Account does not have details associated with it.")
        schema = AccountDetailSchema()
        return {'account_detail':schema.dump(account_detail)}

class RoleList(Resource):
    method_decorators = [auth_role('admin'), jwt_required()]
    def get(self):
        roles = Role.query.all()
        schema = RoleSchema(many=True)
        return {'roles':schema.dump(roles)}

class AccountRoleList(Resource):
    method_decorators = [auth_role('admin'), jwt_required()]
    def get(self):
        account_roles = AccountRole.query.all()
        schema = AccountRoleSchema(many=True)
        return {'account_roles': schema.dump(account_roles)}
    
    method_decorators = [auth_role('admin'), jwt_required()]
    def post(self):
        schema = AccountRoleSchema()
        validated_data = schema.load(request.json)
        account_role = AccountRole(**validated_data)

        db.session.add(account_role)
        db.session.commit()

        return {'msg':'Account Role Created', 'account_role': schema.dump(account_role)}

class AccountRoleResource(Resource):
    method_decorators = [auth_role('admin'), jwt_required()]
    def get(self, account_id):
        account_role = AccountRole.query.filter_by(account_id=account_id).first_or_404('This account does not have a special role.')
        schema = AccountRoleSchema()
        return {'account_role': schema.dump(account_role)}
    
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

