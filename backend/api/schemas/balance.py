from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import Integer

from extensions import db
from models.balances import Balance
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class AdminViewBalanceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Balance
        sqla_session = db.session

class BalanceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Balance
        load_instance = True
        exclude = ['id', 'account_id']
        sqla_session = db.session

class BalanceCreateSchema(BalanceSchema):
    amount = Integer(
        required=True,
        validate=[
            validate.Range(1, error='Amount in starting balance must be positive and greater than zero.')
        ]
    )