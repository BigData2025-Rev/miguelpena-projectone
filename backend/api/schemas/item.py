from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import String, Nested

from extensions import db
from models import Item
from schemas import CategorySchema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class ItemSchema(SQLAlchemyAutoSchema):
    category = Nested(CategorySchema)

    class Meta:
        model = Item
        sqla_session = db.session
        exclude = ['id', 'category_id']
        load_instance = True
        include_relationships = True

class AdminItemSchema(SQLAlchemyAutoSchema):
    category = Nested(CategorySchema)

    class Meta:
        model = Item
        sqla_session = db.session
        load_instance = True
        include_relationships = True