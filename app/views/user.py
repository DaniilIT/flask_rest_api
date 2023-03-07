from flask import request
from flask_restx import Resource, Namespace

from app.dao.models.user import UserSchema
from app.implemented import user_service

user_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        users = user_service.get_all()
        return users_schema.dump(users), 200

    def post(self):
        req_json = request.json
        user_id = user_service.create(req_json)
        return '', 201, {'location': f'/movies/{user_id}'}


@user_ns.route('/<int:user_id>')
class UserView(Resource):
    def get(self, user_id: int):
        user = user_service.get_one(user_id)
        return user_schema.dump(user), 200

    def put(self, user_id: int):
        req_json = request.json
        req_json['id'] = user_id
        user_service.update(req_json)
        return '', 204  # No Response

    def patch(self, user_id: int):
        req_json = request.json
        req_json['id'] = user_id
        user_service.update_partial(req_json)
        return '', 204  # No Response

    def delete(self, user_id: int):
        user_service.delete(user_id)
        return '', 204  # No Response
