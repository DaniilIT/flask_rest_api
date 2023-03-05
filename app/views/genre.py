from flask_restx import Resource, Namespace
from app.implemented import genre_service
from app.dao.models.genre import GenreSchema


genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    def get(self, genre_id: int):
        genre = genre_service.get_one(genre_id)
        return genre_schema.dump(genre), 200
