from marshmallow import post_load, ValidationError
from marshmallow.fields import Integer, Nested

from extensions import db
from models import Order, Item
from schemas import AdminItemSchema, ItemSchema, AdminAccountViewSchema, AccountSchema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class AdminOrderViewSchema(SQLAlchemyAutoSchema):
    item = Nested(AdminItemSchema)
    account = Nested(AdminAccountViewSchema)
    
    class Meta:
        model = Order
        sqla_session = db.session
        include_relationships = True

class OrderSchema(SQLAlchemyAutoSchema):
    item = Nested(ItemSchema)
    account = Nested(AccountSchema)

    class Meta:
        model = Order
        exclude = ['account_id', 'item_id']
        sqla_session = db.session
        include_relationships = True

class CreateOrderSchema(SQLAlchemyAutoSchema):
    item_id = Integer(required=True)
    quantity = Integer(required=True)
    account_id = Integer(required=False)

    class Meta:
        model = Order
        load_instance = True
        include_relationships = True
        sqla_session = db.session

    @post_load
    def calculate_total(self, data, **kwargs):
        item = Item.query.get(data.get('item_id'))
        if not item:
            raise ValidationError('Item does not exist.')
        
        data['total'] = item.cost * data.get('quantity')
        return data