from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import String

from extensions import ma
from models import Item, ItemCategory
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class ItemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Item

class ItemCategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ItemCategory