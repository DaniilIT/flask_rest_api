from .models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, movie_id):
        movie = self.session.query(Movie).get(movie_id)
        return movie

    def get_all(self, year=None, genre_id=None, director_id=None):
        movies = self.session.query(Movie)
        if year:
            year = int(year)
            movies = movies.filter(Movie.year == year)
        if genre_id:
            genre_id = int(genre_id)
            movies = movies.filter(Movie.genre_id == genre_id)
        if director_id:
            director_id = int(director_id)
            movies = movies.filter(Movie.director_id == director_id)
        movies = movies.all()
        return movies

    def create(self, req_json):
        movie = Movie(**req_json)
        self.session.add(movie)
        self.session.commit()
        return movie.id

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, movie):
        self.session.delete(movie)
        self.session.commit()
