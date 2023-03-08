import base64
import hashlib
import hmac

from app.dao.user import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, user_id):
        user = self.dao.get_one(user_id)
        return user

    def get_by_username(self, username):
        user = self.dao.get_by_username(username)
        return user

    def get_all(self, **args):
        users = self.dao.get_all(**args)
        return users

    def create(self, user_dict):
        user_dict['password'] = self.generate_password_hash(user_dict.get('password'))
        user_id = self.dao.create(user_dict)
        return user_id

    def update(self, user_dict):
        user_id = user_dict.get('id')
        user = self.get_one(user_id)

        user.username = user_dict.get('username')
        user.password = self.generate_password_hash(user_dict.get('password'))
        user.role = user_dict.get('role')

        self.dao.update(user)

    def update_partial(self, user_dict):
        user_id = user_dict.get('id')
        user = self.get_one(user_id)

        if 'username' in user_dict:
            user.username = user_dict['username']
        if 'password' in user_dict:
            user.password = self.generate_password_hash(user_dict['password'])
        if 'role' in user_dict:
            user.role = user_dict['role']

        self.dao.update(user)

    def delete(self, user_id):
        user = self.get_one(user_id)

        self.dao.delete(user)

    def get_hash_digest(self, password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

    def generate_password_hash(self, password):
        hash_digest = self.get_hash_digest(password)
        return base64.b64encode(hash_digest)

    def compare_passwords(self, password_hash, other_password) -> bool:
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            self.get_hash_digest(other_password)
        )
