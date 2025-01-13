from flask import Blueprint, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from api.resources import *

blueprint = Blueprint('api', __name__, url_prefix='/pokemart')
api = Api(blueprint, errors=blueprint.errorhandler)

api.add_resource(AccountList, '/accounts')
api.add_resource(BalanceList, '/balance')

# api.add_resource(AccountResource, '/accounts/<username>')

"""
    TODO:
        - endpoints for orders
        - endpoints for items
        - endpoints balance
        - endpoints for account details
        - endpoints for roles
"""

@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return jsonify(e.messages), 400