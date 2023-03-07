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

    def create(self, req_json):
        genre = Genre(**req_json)
        self.session.add(genre)
        self.session.commit()
        return genre.id

    def update(self, genre):
        self.session.add(genre)
        self.session.commit()

    def delete(self, genre):
        self.session.delete(genre)
        self.session.commit()
