from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import String

from extensions import ma
from models.items import Item
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class ItemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Item