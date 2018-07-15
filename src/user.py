from flask import jsonify, redirect, request
from flask_restful import Resource, Api
from src import app
from src import db
from src.auth import auth
from src.models import users

api = Api(app)


class RUser(Resource):

    @auth.requires_auth
    def get(self):
        email = request.args.get('email')
        user = users.User.query.filter_by(email=email).first()

        return jsonify({'err': 0, 'err_msg': '', 'name': user.name})

    def post(self):
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user = users.User(name, email, password)
        db.session.add(user)
        db.session.commit()

        return jsonify({'err': 0, 'err_msg': 'Insert successful.'})

    @auth.requires_auth
    def put(self):
        email = request.form['email']
        name = request.form['name']
        user = users.User.query.filter_by(email=email).first()
        user.name = name
        db.session.commit()

        return jsonify({'err': 0, 'err_msg': 'Update successful.'})

    @auth.requires_auth
    def delete(self):
        email = request.form['email']
        user = users.User.query.filter_by(email=email).first()
        user.status = -1
        db.session.commit()

        return jsonify({'err': 0, 'err_msg': 'Delete successful.'})


api.add_resource(RUser, '/user')
