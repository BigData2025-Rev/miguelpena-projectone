from marshmallow import validate, validates_schema, ValidationError, pre_load
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
        include_fk = True

class BalanceCreateSchema(BalanceSchema):
    account_id = Integer(required=True)

    amount = Integer(
        required=True,
        validate=[
            validate.Range(1, error='Amount in starting balance must be positive and greater than zero.')
        ]
    )

    @pre_load
    def add_account_id(self, data, **kwargs):
        if "account_id" not in data and "account_id" in self.context:
            data["account_id"] = self.context["account_id"]
        return data