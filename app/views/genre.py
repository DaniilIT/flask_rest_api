from flask import request
from flask_restx import Resource, Namespace

from app.dao.models.genre import GenreSchema
from app.decorators import auth_required, admin_required
from app.implemented import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200

    @admin_required
    def post(self):
        req_json = request.json
        genre_id = genre_service.create(req_json)
        return '', 201, {'location': f'/genres/{genre_id}'}


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    @auth_required
    def get(self, genre_id: int):
        genre = genre_service.get_one(genre_id)
        return genre_schema.dump(genre), 200

    @admin_required
    def put(self, genre_id: int):
        req_json = request.json
        req_json['id'] = genre_id
        genre_service.update(req_json)
        return '', 204  # No Response

    @admin_required
    def patch(self, genre_id: int):
        req_json = request.json
        req_json['id'] = genre_id
        genre_service.update_partial(req_json)
        return '', 204  # No Response

    @admin_required
    def delete(self, genre_id: int):
        genre_service.delete(genre_id)
        return '', 204  # No Response
