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
    
class AccountResource(Resource):
    method_decorators = [auth_role('admin'), jwt_required()]
    def delete(self, account_id):
        account = Account.query.get(account_id)
        if account is None:
            return {'msg':'Account does not exist!'}, 400

        db.session.delete(account)
        db.session.commit()

        return {'msg':'Account Deleted'}

class ProfileResource(Resource):
    method_decorators = [jwt_required()]
    def get(self):
        account_id = get_jwt_identity()
        profile = Profile.query.filter_by(account_id=account_id).first_or_404("Account does not have a profile associated with it.")
        schema = ProfileSchema()
        return {'profile': schema.dump(profile)}
    
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
    
    method_decorators = [jwt_required()]
    def put(self):
        schema = ProfileSchema(partial=True)
        account_id = get_jwt_identity()
        profile = Profile.query.filter_by(account_id=account_id).first_or_404('This account does not have a profile.')
        profile = schema.load(request.json, instance=profile)
        
        db.session.add(profile)
        db.session.commit()

        return {'msg':'Profile was Updated.', 'profile': schema.dump(profile)}

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
    def delete(self, account_id):
        account_role = AccountRole.query.filter_by(account_id=account_id).first_or_404('This account is not an admin.')
        schema = AccountRoleSchema()
        db.session.delete(account_role)
        db.session.commit()

        return {'msg':'Account Role Deleted', 'account_role': schema.dump(account_role)}



