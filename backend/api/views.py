from flask import Blueprint
from flask_restful import Api

from api.resources.account import AccountList, AccountResource

blueprint = Blueprint('api', __name__, url_prefix='/pokemart/')
api = Api(blueprint, errors=blueprint.errorhandler)

api.add_resource(AccountList, '/accounts/')
api.add_resource(AccountResource, '/accounts/<int:account_id>')