from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from api.schemas import OrderSchema
from extensions import db
from auth.decorators import auth_role
from models import Order

class OrderList(Resource):
    pass

class OrderResource(Resource):
    method_decorators = [jwt_required()]
    def post(self):
        data = request.get_json()
        # Assuming you have an Order model and OrderSchema
        order_schema = OrderSchema()
        order = order_schema.load(data)
        
        db.session.add(order)
        db.session.commit()
        
        return order_schema.dump(order), 201
    
class CreateOrderResource(Resource):
    pass

class AdminOrderList(Resource):
    pass