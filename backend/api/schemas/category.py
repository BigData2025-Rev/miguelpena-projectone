from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import String, Nested

from extensions import db
from models.categories import Category
import api.schemas.item as sub_items
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class CategoryWithItemsSchema(SQLAlchemyAutoSchema):
    items = Nested(sub_items.ItemSchema, many=True, allow_none=True)

    class Meta:
        model = Category
        sqla_session = db.session
        include_fk = False
        include_relationships = True

class CategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        sqla_session = db.session
