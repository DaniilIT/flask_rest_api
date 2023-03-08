from .models.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, user_id):
        user = self.session.query(User).get(user_id)
        return user

    def get_by_username(self, username):
        user = self.session.query(User).filter(User.username == username).first()
        return user

    def get_all(self):
        users = self.session.query(User).all()
        return users

    def create(self, req_json):
        user = User(**req_json)
        self.session.add(user)
        self.session.commit()
        return user.id

    def update(self, user):
        self.session.add(user)
        self.session.commit()

    def delete(self, user):
        self.session.delete(user)
        self.session.commit()
