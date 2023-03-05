from .models.genre import Genre


class GenreDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, genre_id):
        genre = self.session.query(Genre).get(genre_id)
        return genre

    def get_all(self):
        genres = self.session.query(Genre).all()
        return genres
