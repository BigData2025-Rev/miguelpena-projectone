from extensions import db

class Category(db.Model):
    __tablename__ = 'item_categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(50), nullable=False, unique=True)

    items = db.relationship('Item', back_populates='category', lazy=True, cascade="all, delete-orphan")