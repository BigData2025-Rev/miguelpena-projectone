from extensions import db

class Category(db.Model):
    __tablename__ = 'item_categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(50), nullable=False, unique=True)

    items = db.relationship('Item', backref='category', lazy=True, cascade="all, delete-orphan")

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    cost = db.Column(db.Integer, nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('item_categories.id'), nullable=False)