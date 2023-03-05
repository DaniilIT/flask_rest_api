from flask import request, jsonify
from flask_restx import Resource, Namespace

from app.implemented import movie_service
from app.dao.models.movie import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = movie_service.get_all(
            year=request.args.get('year'),
            genre_id=request.args.get('genre_id'),
            director_id=request.args.get('director_id')
        )
        return movies_schema.dump(movies), 200

    def post(self):
        req_json = request.json
        movies_id = movie_service.create(req_json)
        response = jsonify()
        response.status_code = 201
        response.headers['location'] = f'/movies/{movies_id}'
        return '', 201, {'location': f'/movies/{movies_id}'}  # response


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id: int):
        movie = movie_service.get_one(movie_id)
        return movie_schema.dump(movie), 200

    def put(self, movie_id: int):
        req_json = request.json
        req_json['id'] = movie_id
        movie_service.update(req_json)
        return '', 204  # No Response

    def patch(self, movie_id: int):
        req_json = request.json
        req_json['id'] = movie_id
        movie_service.update_partial(req_json)
        return '', 204  # No Response

    def delete(self, movie_id: int):
        movie_service.delete(movie_id)
        return '', 204  # No Response
