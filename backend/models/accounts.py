from sqlalchemy.ext.hybrid import hybrid_property
from extensions import db, pwd_context

class Account(db.Model):
    """
        This is the relational model for the user object, 
        should handle database operations with SQLAlchemy's simplified query system, 
        which is similar to Spring Boot's JPARepository which simplified ORM and DAOs. 
    """
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    _password = db.Column("password", db.String(255), nullable=False)
    
    profile = db.relationship('Profile', back_populates='account', uselist=False, passive_deletes=True)
    roles = db.relationship('Role', secondary='account_roles', back_populates='accounts', passive_deletes=True)
    balance = db.relationship('Balance', back_populates='account', uselist=False, passive_deletes=True)
    orders = db.relationship('Order', back_populates='account', lazy=True)

    def has_role(self, role):
        return bool(
            Role.query
            .join(Role.accounts)
            .filter(Account.id == self.id)
            .filter(Role.slug == role)
            .count() == 1
        )

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = pwd_context.hash(value)

class Profile(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer)
    favorite_pokemon = db.Column(db.String(64))

    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id', ondelete='CASCADE'), nullable=False, index=True)
    
    account = db.relationship('Account', back_populates='profile', uselist=False, passive_deletes=True)

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(36), nullable=False)
    slug = db.Column(db.String(36), nullable=False, unique=True)

    accounts = db.relationship("Account", secondary="account_roles", back_populates="roles", passive_deletes=True)

    def __repr__(self):
        return f"{self.__class__.__name__}, name: {self.name}"
    
class AccountRole(db.Model):
    __tablename__ = "account_roles"

    user_id = db.Column(db.Integer, db.ForeignKey("accounts.id", ondelete="CASCADE"), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True)