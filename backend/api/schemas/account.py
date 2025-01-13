from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import String

from extensions import db
from models.accounts import Account, AccountDetail, AccountRole, Role
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
        exclude = ['id', '_password']
        sqla_session = db.session

class AccountCreateSchema(AccountSchema):
    password = String(
        required=True,
        validate=[
            validate.Regexp(r"^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9])(?=.*[a-z]).{8,}$",
                                error="The password needs to be at least 8 characters long, and include a lowercase, uppercase, number and special character.")
        ]
    )

class AccountDetailSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = AccountDetail
        load_instance = True
        exclude = ['id', 'account_id']
        sqla_session = db.session

class RoleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        load_instance = True
        exclude = ['id']
        sqla_session = db.session

class AccountRoleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = AccountRole
        load_instance = True
        sqla_session = db.session