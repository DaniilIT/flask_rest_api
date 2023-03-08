from .models.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, director_id):
        director = self.session.query(Director).get(director_id)
        return director

    def get_all(self):
        directors = self.session.query(Director).all()
        return directors

    def create(self, req_json):
        director = Director(**req_json)
        self.session.add(director)
        self.session.commit()
        return director.id

    def update(self, director):
        self.session.add(director)
        self.session.commit()

    def delete(self, director):
        self.session.delete(director)
        self.session.commit()
