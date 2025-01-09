from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import Integer

from extensions import ma
from models.balances import Balance
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class BalanceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Balance
        load_instance = True
        exclude = ['id', 'account_id']

class BalanceCreateSchema(BalanceSchema):
    amount = Integer(
        required=True,
        validate=[
            validate.Range(1, error='Amount in starting balance must be positive and greater than zero.')
        ]
    )