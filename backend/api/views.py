from flask import Blueprint, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from api.resources import *

blueprint = Blueprint('api', __name__, url_prefix='/pokemart')
api = Api(blueprint, errors=blueprint.errorhandler)

api.add_resource(AccountList, '/users') # admin only
api.add_resource(BalanceList, '/balance')

# api.add_resource(AccountResource, '/accounts/<username>')

"""
    TODO:
        - add the following endpoints:
            - /users -> methods = ['GET', 'DELETE']
            - /user_roles -> methods = ['POST', 'DELETE']
            - /balance -> methods = ['GET', 'PUT']
            - /
"""

@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return jsonify(e.messages), 400