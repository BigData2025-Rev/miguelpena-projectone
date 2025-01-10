from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from api.schemas import ItemSchema, ItemCategorySchema
from extensions import db
from auth.decorators import auth_role
from models import Item, ItemCategory

class ItemList(Resource):
    method_decorators = [auth_role(['user','admin']), jwt_required()]
    def get(self):
        items = Item.query.all() #equivalent to running SELECT * FROM items;
        schema = ItemSchema(many=True)
        return {'results': schema.dump(items)}
    
    method_decorators = [auth_role('admin'), jwt_required()]
    def post(self):
        schema = ItemSchema()
        validated_data = schema.load(request.json)
        item = Item(**validated_data)

        db.session.add(item)
        db.session.commit() #adds ACID properties to SQL database.

        return {'msg':'Item Created', 'item':schema.dump(item)}
    
class ItemCategoryList(Resource):
    method_decorators = [auth_role(['user', 'admin']), jwt_required()]
    def get(self):
        categories = ItemCategory.query.all()
        schema = ItemCategorySchema(many=True)
        return {'results': schema.dump(categories)}
    