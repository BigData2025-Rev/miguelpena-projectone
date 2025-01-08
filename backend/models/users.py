from dataclasses import dataclass

from extensions import db

class User(db.Model):
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
    id: int
    username: str
    password: str
    # user_detail_id: int

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)
    # user_detail_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
