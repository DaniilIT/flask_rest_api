from app.dao.genre import GenreDao


class GenreService:
    def __init__(self, dao: GenreDao):
        self.dao = dao

    def get_one(self, genre_id):
        genre = self.dao.get_one(genre_id)
        return genre

    def get_all(self):
        genres = self.dao.get_all()
        return genres
