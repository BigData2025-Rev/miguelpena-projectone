from extensions import db

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    cost = db.Column(db.Integer, nullable=False)

    category = db.relationship('ItemCategory', secondary="item_category_relational", back_populates="item", passive_deletes=True)
    orders = db.relationship('Order', back_populates='item')

class ItemCategory(db.Model):
    __tablename__ = 'item_categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(50), nullable=False, unique=True)

    item = db.relationship('Item', secondary='item_category_relational', back_populates='category', passive_deletes=True)

class ItemCategoryRelational(db.Model):
    __tablename__ = 'item_category_relational'

    item_id = db.Column(db.Integer, db.ForeignKey("items.id", ondelete="CASCADE"), primary_key=True)
    item_category_id = db.Column(db.Integer, db.ForeignKey("item_categories.id", ondelete="CASCADE"), primary_key=True)