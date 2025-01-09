from sqlalchemy.ext.hybrid import hybrid_property
from extensions import db, pwd_context

class Account(db.Model):
    """
        This is the relational model for the user object, 
        should handle database operations with SQLAlchemy's simplified query system, 
        which is similar to Spring.
        
        TODO:
            - Make sure that the frontend hashes the password before passing it to the api.
            - Make sure that this model is updated as more models are added,
                for example, user_detail_id should be a foreignkey that references userdetails.id, 
                which consists of columns id, user_id, first_name, last_name, age
            - Make sure to research one-to-one, one-to-many, and many-to-many relationships for sqlalchemy. 
    """
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    _password = db.Column("password", db.String(255), nullable=False)
    
    account_detail = db.relationship('Account_Detail', back_populates='account', uselist=False, passive_deletes=True)
    roles = db.relationship('Role', secondary='account_roles', back_populates='accounts', passive_deletes=True)
    balance = db.relationship('Balance', back_populates='account', uselist=False, passive_deletes=True)
    orders = db.relationship('Order', back_populates='account', lazy=True)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = pwd_context.hash(value)

class Account_Detail(db.Model):
    __tablename__ = 'account_details'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id', ondelete='CASCADE'), nullable=False, index=True)
    
    account = db.relationship('Account', back_populates='account_detail', uselist=False, passive_deletes=True)

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