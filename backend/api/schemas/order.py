from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import String

from extensions import db
from models import Order, Item
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class AdminOrderViewSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Order

        sqla_session = db.session

class OrderSchema(SQLAlchemyAutoSchema):

    @validates_schema
    def validate_item(self, data, **kwargs):
        item_id = data.get('item_id')

        if Item.query.get(item_id) == None:
            raise ValidationError(f'Item must exist.')


    class Meta:
        model = Order

        exclude = ['account_id']
        sqla_session = db.session

class CreateOrderSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance = True
        sqla_session = db.session