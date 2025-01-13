from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from api.schemas import AdminItemSchema, ItemSchema, CategorySchema, CategoryWithItemsSchema
from extensions import db
from auth.decorators import auth_role
from models import Item, Category

class ItemList(Resource):
    method_decorators = [jwt_required()]
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

class ItemResource(Resource):
    def get(self, category):
        category_obj = Category.query.filter_by(slug=category).first_or_404('This category doesn\'t have any items')
        schema = CategoryWithItemsSchema()
        return {'results': schema.dump(category_obj)}

class CategoryList(Resource):
    method_decorators = [jwt_required()]
    def get(self):
        categories = Category.query.all()
        schema = CategorySchema(many=True)
        return {'results': schema.dump(categories)}

class AdminItemList(Resource):
    method_decorators = [auth_role('admin'), jwt_required()]
    def get(self):
        items = Item.query.all() #equivalent to running SELECT * FROM items;
        schema = AdminItemSchema(many=True)
        return {'results': schema.dump(items)}
    
    method_decorators = [auth_role('admin'), jwt_required()]
    def post(self):
        schema = AdminItemSchema()
        validated_data = schema.load(request.json)

        item = Item(**validated_data)

        db.session.add(item)
        db.session.commit()
        
        return {'msg':'Inventory Item Created', 'item': schema.dump(item)}

class AdminItemResource(Resource):
    method_decorators = [auth_role('admin'), jwt_required()]
    def put(self, item_id):
        schema = AdminItemSchema(partial=True)
        item = Item.query.get_or_404(item_id, description='That item does not exist.')
        item = schema.load(request.json, instance=item)

        db.session.add(item)
        db.session.commit()

        return {'msg':'Item Updated', 'item': schema.dump(item)}

    method_decorators = [auth_role('admin'), jwt_required()]
    def delete(self, item_id):
        item = Item.query.get_or_404(item_id, description='That item does not exist.')
        schema = AdminItemSchema()

        db.session.delete(item)
        db.session.commit()

        return {'msg':'Item Deleted', 'item': schema.dump(item)}