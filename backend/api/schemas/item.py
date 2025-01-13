from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import String

from extensions import db
from models import Item, ItemCategory
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class ItemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        sqla_session = db.session

class ItemCategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ItemCategory
        sqla_session = db.session