from flask import request, jsonify
from flask_restful import Resource, abort
from flask_jwt_extended import jwt_required, get_jwt_identity

from api.schemas import AccountSchema, AdminAccountViewSchema, ProfileSchema, AccountRoleSchema, RoleSchema
from extensions import db
from auth.decorators import auth_role
from models import Account, Profile, AccountRole, Role

class AccountList(Resource):
    method_decorators = [auth_role('admin'), jwt_required()]
    def get(self):
        accounts = Account.query.all() #equivalent to running SELECT * FROM accounts;
        schema = AdminAccountViewSchema(many=True)
        return {'results': schema.dump(accounts)}
    
class ProfileList(Resource):
    method_decorators = [jwt_required()]
    def post(self):
        schema = ProfileSchema()
        validated_data = schema.load(request.json)
        account_id = get_jwt_identity()

        validated_data['account_id'] = account_id

        profile = Profile(**validated_data)
        
        db.session.add(profile)
        db.session.commit()

        return {'msg':'Profile was created.', 'profile': schema.dump(profile)}
    
class ProfileAdminResource(Resource):
    method_decorators = [auth_role('admin'), jwt_required()]
    def get(self, account_id):
        profile = Profile.query.filter_by(account_id=account_id).first_or_404("Account does not have a profile associated with it.")
        schema = AdminProfileSchema()
        return {'profile': schema.dump(profile)}

class ProfileResource(Resource):
    method_decorators = [jwt_required()]
    def get(self):
        account_id = get_jwt_identity()
        profile = Profile.query.filter_by(account_id=account_id).first_or_404("Account does not have a profile associated with it.")
        schema = ProfileSchema()
        return {'profile': schema.dump(profile)}

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

