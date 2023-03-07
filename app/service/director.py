from app.dao.director import DirectorDao


class DirectorService:
    def __init__(self, dao: DirectorDao):
        self.dao = dao

    def get_one(self, director_id):
        director = self.dao.get_one(director_id)
        return director

    def get_all(self):
        directors = self.dao.get_all()
        return directors

    def create(self, req_json):
        director_id = self.dao.create(req_json)
        return director_id

    def update(self, req_json):
        director_id = req_json.get('id')
        director = self.get_one(director_id)

        director.name = req_json.get('name')

        self.dao.update(director)

    def update_partial(self, req_json):
        director_id = req_json.get('id')
        director = self.get_one(director_id)

        if 'name' in req_json:
            director.username = req_json['name']

        self.dao.update(director)

    def delete(self, director_id):
        director = self.get_one(director_id)

        self.dao.delete(director)
