from flask import request
from flask_restx import Resource, Namespace

from app.dao.models.director import DirectorSchema
from app.implemented import director_service
from app.decorators import auth_required, admin_required

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200

    @admin_required
    def post(self):
        req_json = request.json
        director_id = director_service.create(req_json)
        return '', 201, {'location': f'/directors/{director_id}'}


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):
    @auth_required
    def get(self, director_id: int):
        director = director_service.get_one(director_id)
        return director_schema.dump(director), 200

    @admin_required
    def put(self, director_id: int):
        req_json = request.json
        req_json['id'] = director_id
        director_service.update(req_json)
        return '', 204  # No Response

    @admin_required
    def patch(self, director_id: int):
        req_json = request.json
        req_json['id'] = director_id
        director_service.update_partial(req_json)
        return '', 204  # No Response

    @admin_required
    def delete(self, director_id: int):
        director_service.delete(director_id)
        return '', 204  # No Response
