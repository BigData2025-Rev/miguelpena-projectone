from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import String

from extensions import ma
from models.balances import Balance
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class BalanceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Balance