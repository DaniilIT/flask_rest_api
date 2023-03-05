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
