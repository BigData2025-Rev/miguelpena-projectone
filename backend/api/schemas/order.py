from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import String

from extensions import db
from models.orders import Order
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class OrderSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        sqla_session = db.session