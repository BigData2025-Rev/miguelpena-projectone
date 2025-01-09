from flask import Flask

from api.views import blueprint
from extensions import db, ma, migrate, jwt

app = Flask(__name__)
app.register_blueprint(blueprint=blueprint)
app.config.from_object('config')

db.init_app(app)
ma.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)

if __name__ == '__main__':
    app.run(
        host=app.config.get('FLASK_RUN_HOST'),
        port=app.config.get('FLASK_RUN_PORT'),
        debug=app.config.get('FLASK_DEBUG')
    )

"""
    REMINDER:
        - Remove migrate and its folders once the database is completed. 
            It is only necessary for whenever you make changes to the database schema, 
            and don't feel like reseeding the database.


    This is main entry point for the backend. Open a powershell, and run:
    python app.py

    The api should then run in the background.
"""