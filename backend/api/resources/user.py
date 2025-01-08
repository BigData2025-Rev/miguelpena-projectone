from flask import request, jsonify
from flask_restful import Resource, abort

from extensions import db
from models.users import User

class UserList(Resource):
    def get(self):
        users = User.query.all() #equivalent to running SELECT * FROM users;
        return jsonify(results=users)
    
    def post(self):
        data = request.json
        #validation of data will mostly occur in the frontend for now, but I can add an additional layer of security with FLask-Marshmellow
        user = User(
            username=data.get('username'),
            password=data.get('password')
        )

        db.session.add(user)
        db.session.commit() #adds ACID properties to SQL database.

        return jsonify(msg='User Created', user=user)
    
class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id) #equivalent to SELECT * FROM users WHERE users.id=?; where ? is usually replaced with user_id in Spring.

        return jsonify(user=user)
    
    def put(self, user_id):
        data = request.json

        user = User.query.get_or_404(user_id)
        user.password = data.get('password') #the setter for the user object triggers an DML query: UPDATE users SET users.password=? WHERE users.id=?; 

        db.session.commit()

        return jsonify(msg='User Updated', user=user)
    
    def delete(self, user_id):
        user = User.query.get_or_404(user_id)

        db.session.delete(user) #triggers a DML query: DELETE FROM users WHERE users.id=?; Typically, NOTE: ondelete='CASCADE' property will maintain referential integrity.
        db.session.commit()

        return jsonify(msg='User Deleted')

