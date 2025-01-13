from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import String, Nested

from extensions import db
from models.items import Item
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class ItemSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = Item
        sqla_session = db.session
        exclude = ['id', 'category_id']
        load_instance = True
        include_relationships = True

class AdminItemSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = Item
        sqla_session = db.session
        load_instance = True
        include_relationships = True