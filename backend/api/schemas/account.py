from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import String

from extensions import ma
from models.accounts import Account
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class AccountSchema(SQLAlchemyAutoSchema):
    username = String(required=True, validate=[validate.Length(min=3)])

    @validates_schema
    def validate_username(self, data, **kwargs):
        username = data.get('username')

        if Account.query.filter_by(username=username).count():
            raise ValidationError(f'Username {username} already exists.')

    class Meta:
        model = Account
        load_instance = True
        exclude = ['id']