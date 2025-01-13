from flask import Blueprint, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from api.resources import *

blueprint = Blueprint('api', __name__, url_prefix='/pokemart')
api = Api(blueprint, errors=blueprint.errorhandler)

api.add_resource(AccountList, '/users') # admin only -> GET
api.add_resource(AccountResource, '/users/<int:account_id>') #admin only -> DELETE

api.add_resource(AccountRoleList, '/user_role') #admin only -> POST
api.add_resource(AccountRoleResource, '/user_role/<int:account_id>') #admin only -> DELETE

api.add_resource(BalanceList, '/balances') #admin only -> GET, login-required -> POST
api.add_resource(BalanceResource, '/balance')

api.add_resource(ProfileResource, '/profile')

api.add_resource(CategoryList, '/categories')

api.add_resource(ItemList, '/store')

api.add_resource(AdminItemList, '/store/inventory') #admin only -> GET, POST
api.add_resource(AdminItemResource, '/store/inventory/<int:item_id>') #admin only -> PUT and DELETE

api.add_resource(ItemResource, '/store/<str:category>')

api.add_resource(CreateOrderResource, '/store/checkout')
api.add_resource(OrderList, '/history')

api.add_resource(AdminOrderList, '/store/orders') #admin only -> GET

@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return jsonify(e.messages), 400