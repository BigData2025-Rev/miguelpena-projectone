from extensions import db
from models import Category

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    cost = db.Column(db.Integer, nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('item_categories.id'), nullable=False)

    category = db.relationship('Category')