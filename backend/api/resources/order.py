from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from api.schemas.order import AdminOrderViewSchema, OrderSchema, CreateOrderSchema
from extensions import db
from auth.decorators import auth_role
from models import Order, Balance

class OrderList(Resource):
    method_decorators = [jwt_required()]
    def get(self):
        account_id = get_jwt_identity()
        orders = Order.query.filter_by(account_id=account_id).all()
        schema = OrderSchema(many=True)

        return {'results': schema.dump(orders)}

class OrderResource(Resource):
    method_decorators = [jwt_required()]
    def delete(self, order_id):
        order = Order.query.get_or_404(order_id)
        account_id = get_jwt_identity()
        balance = Balance.query.filter_by(account_id=account_id).first_or_404('Account does not have a balance.')
        balance.amount += order.total
        
        schema = OrderSchema()
        
        db.session.delete(order)
        db.session.commit()

        return {'msg':'Order Canceled, and Refund Issued', 'order': schema.dump(order)}
    
class CreateOrderResource(Resource):
    method_decorators = [jwt_required()]
    def post(self):
        account_id = get_jwt_identity()
        schema = CreateOrderSchema()
        validated_data = schema.load(request.json)
        validated_data['account_id'] = account_id
        balance = Balance.query.filter_by(account_id=account_id).first_or_404('Account does not have a balance.')
        order = Order(**validated_data)
        if balance.amount - order.total < 0:
            return {'msg':'Order Canceled: Not Enough Funds'}, 400
        
        balance.amount -= order.total

        db.session.add(order)
        db.session.commit()
        
        return {'msg': 'Order Created', 'order': schema.dump(order)}

class AdminOrderList(Resource):
    method_decorators = [auth_role('admin'), jwt_required()]
    def get(self):
        orders = Order.query.all()
        schema = AdminOrderViewSchema(many=True)
        return {'results': schema.dump(orders)}