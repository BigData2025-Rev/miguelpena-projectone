from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import String, Nested

from extensions import db
from schemas import AdminViewBalanceSchema, BalanceSchema
from models import Account, Profile, AccountRole, Role
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class AdminProfileSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Profile
        sqla_session = db.session
        include_fk = True

class AdminAccountViewSchema(SQLAlchemyAutoSchema):
    profile = Nested(AdminProfileSchema, allow_none=True)
    balance = Nested(AdminViewBalanceSchema, allow_none=True)

    class Meta:
        model = Account
        exclude = ['_password']
        sqla_session = db.session
        load_instance = True
        include_relationships = True

class ProfileSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Profile
        load_instance = True
        include_fk = False
        exclude = ['id', 'account_id']
        sqla_session = db.session

class AccountSchema(SQLAlchemyAutoSchema):
    profile = Nested(ProfileSchema, allow_none=True)
    balance = Nested(BalanceSchema, allow_none=True)

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
        include_relationships = True

class AccountCreateSchema(AccountSchema):
    password = String(
        required=True,
        validate=[
            validate.Regexp(r"^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9])(?=.*[a-z]).{8,}$",
                                error="The password needs to be at least 8 characters long, and include a lowercase, uppercase, number and special character.")
        ]
    )




class RoleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        sqla_session = db.session

class AccountRoleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = AccountRole
        sqla_session = db.session