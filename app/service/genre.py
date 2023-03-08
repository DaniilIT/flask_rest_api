from app.dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, genre_id):
        genre = self.dao.get_one(genre_id)
        return genre

    def get_all(self):
        genres = self.dao.get_all()
        return genres

    def create(self, req_json):
        genre_id = self.dao.create(req_json)
        return genre_id

    def update(self, req_json):
        genre_id = req_json.get('id')
        genre = self.get_one(genre_id)

        genre.name = req_json.get('name')

        self.dao.update(genre)

    def update_partial(self, req_json):
        genre_id = req_json.get('id')
        genre = self.get_one(genre_id)

        if 'name' in req_json:
            genre.username = req_json['name']

        self.dao.update(genre)

    def delete(self, genre_id):
        genre = self.get_one(genre_id)

        self.dao.delete(genre)
