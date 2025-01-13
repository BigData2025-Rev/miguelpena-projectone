from sqlalchemy import text
from app import db, app

def load_seed_data():
    with open('seed.sql', 'r') as file:
        seed_sql = file.read()

    statements = seed_sql.split(';')
    
    with app.app_context():
        db.session.execute(text("ALTER TABLE roles AUTO_INCREMENT = 1;"))
        db.session.commit()

        db.session.execute(text('INSERT INTO roles(name, slug) VALUES (\'Admin\', \'admin\');'))
        db.session.commit()

        db.session.execute(text("ALTER TABLE items AUTO_INCREMENT = 1;")) 
        db.session.commit()

        db.session.execute(text("ALTER TABLE item_categories AUTO_INCREMENT = 1;")) 
        db.session.commit()

        for statement in statements:
            if statement.strip():
                db.session.execute(text(statement))
                db.session.commit()
        
        

if __name__ == '__main__':
    load_seed_data()
    print("Seed data loaded successfully.")