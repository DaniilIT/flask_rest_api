from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, movie_id):
        movie = self.dao.get_one(movie_id)
        return movie

    def get_all(self, **args):
        movies = self.dao.get_all(**args)
        return movies

    def create(self, req_json):
        movie_id = self.dao.create(req_json)
        return movie_id

    def update(self, req_json):
        movie_id = req_json.get('id')
        movie = self.get_one(movie_id)

        movie.title = req_json.get('title')
        movie.description = req_json.get('description')
        movie.trailer = req_json.get('trailer')
        movie.year = req_json.get('year')
        movie.rating = req_json.get('rating')
        movie.genre_id = req_json.get('genre_id')
        movie.director_id = req_json.get('director_id')

        self.dao.update(movie)

    def update_partial(self, req_json):
        movie_id = req_json.get('id')
        movie = self.get_one(movie_id)

        if 'title' in req_json:
            movie.title = req_json['title']
        if 'description' in req_json:
            movie.description = req_json['description']
        if 'trailer' in req_json:
            movie.trailer = req_json['trailer']
        if 'year' in req_json:
            movie.year = req_json['year']
        if 'rating' in req_json:
            movie.rating = req_json['rating']
        if 'genre_id' in req_json:
            movie.genre_id = req_json['genre_id']
        if 'director_id' in req_json:
            movie.director_id = req_json['director_id']

        self.dao.update(movie)

    def delete(self, movie_id):
        movie = self.get_one(movie_id)

        self.dao.delete(movie)
