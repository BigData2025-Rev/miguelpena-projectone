from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import String

from extensions import ma
from models.orders import Order
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class OrderSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Order