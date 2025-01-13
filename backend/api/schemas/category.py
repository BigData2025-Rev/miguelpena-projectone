from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import String, Nested

from extensions import db
from models import Category
from schemas import ItemSchema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class CategoryWithItemsSchema(SQLAlchemyAutoSchema):
    items = Nested(ItemSchema, many=True)

    class Meta:
        model = Category
        sqla_session = db.session
        include_fk = False
        include_relationships = True

class CategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        sqla_session = db.session
