from flask import current_app as app
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt
from marshmallow import ValidationError
from api.schemas.account import AccountCreateSchema, AccountSchema
from models.accounts import Account
from extensions import db, pwd_context, jwt

from auth.helpers import add_token_to_database, revoke_token, is_token_revoked

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")

@auth_blueprint.route('/register', methods=['POST'])
def register():
    if not request.is_json:
        return {'msg':'Missing JSON in request'}, 400
    
    schema = AccountCreateSchema()
    account = schema.load(request.json)
    db.session.add(account)
    db.session.commit()

    schema = AccountSchema()

    return {'msg':'Account Created', 'Account': schema.dump(account)}

@auth_blueprint.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return {'msg':'Missing JSON in request'}, 400
    
    username = request.json.get('username')
    password = request.json.get('password')
    if not username or not password:
        return {'msg':'Missing password or email'}, 400
    
    account = Account.query.filter_by(username=username).first()

    if not account or not pwd_context.verify(password, account.password):
        return {'msg':'Bad Credentials'}, 400
    
    access_token = create_access_token(identity=account.id)
    refresh_token = create_refresh_token(identity=account.id)

    add_token_to_database(access_token)
    add_token_to_database(refresh_token)

    return {'access_token': access_token, 'refresh_token': refresh_token}

@auth_blueprint.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    """
        NOTE:
        For frontend, handle the case where access tokens expire after used. When a user login occurs, the api returns an access_token and a refresh_token. 
        The refresh_token should be temporarily saved somewhere by the client, and before making a request to the api, it should access this endpoint and provide 
        the refresh_token, and then use the access_token immediately after to access any resource that the user has access to.
    """
    account_id = get_jwt_identity()
    access_token = create_access_token(identity=account_id)
    add_token_to_database(access_token)
    return {'access_token': access_token}, 200

@auth_blueprint.route('revoke_access', methods=['DELETE'])
@jwt_required()
def revoke_access_token():
    jti = get_jwt()['jti']
    # account = get_current_user()
    account_id = get_jwt_identity()
    revoke_token(jti, account_id)
    return {'msg':'Token Revoked'}, 200

@auth_blueprint.route('revoke_refresh', methods=['DELETE'])
@jwt_required(refresh=True)
def revoke_refresh_token():
    jti = get_jwt()['jti']
    account_id = get_jwt_identity()
    revoke_token(jti, account_id)
    return {'msg':'Refresh Token Revoked'}, 200

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_headers, jwt_payload):
    try:
        return is_token_revoked(jwt_payload)
    except Exception:
        return True

@jwt.user_lookup_loader
def load_account(jwt_headers, jwt_payload):
    account_id = jwt_payload(app.config.get('JWT_IDENTITY_CLAIM'))
    return Account.query.get(account_id)


@auth_blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return jsonify(e.messages), 400