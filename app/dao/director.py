from .models.director import Director


class DirectorDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, director_id):
        director = self.session.query(Director).get(director_id)
        return director

    def get_all(self):
        directors = self.session.query(Director).all()
        return directors
