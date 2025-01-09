from datetime import datetime, timezone

from flask import current_app as app
from flask_jwt_extended import decode_token
from sqlalchemy.exc import NoResultFound

from extensions import db
from models import TokenBlockList

def add_token_to_database(encoded_token):
    decoded_token = decode_token(encoded_token)
    jti = decoded_token['jti']
    token_type = decoded_token['type']
    account_id = decoded_token[app.config.get('JWT_IDENTITY_CLAIM')]
    expires = datetime.fromtimestamp(decoded_token['exp'])

    db_token = TokenBlockList(
        jti=jti,
        token_type=token_type,
        account_id=account_id,
        expires=expires
    )

    db.session.add(db_token)
    db.session.commit()

def revoke_token(token_jti, account_id):
    try:
        token = TokenBlockList.query.filter_by(jti=token_jti, account_id=account_id).one()
        token.revokedat = datetime.now(timezone.utc)
        db.session.commit()
    except NoResultFound:
        raise Exception(f'Could not find token {token_jti}')

def is_token_revoked(jwt_payload):
    jti = jwt_payload['jti']
    account_id = jwt_payload[app.config.get('JWT_IDENTITY_CLAIM')]
    try:
        token = TokenBlockList.query.filter_by(jti=jti, account_id=account_id).one()
        return token.revoked_at is not None
    except NoResultFound:
        raise Exception(f'Could not find token {jti}')