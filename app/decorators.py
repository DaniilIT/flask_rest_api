import jwt
from flask import request, abort
from constants import JWT_SECRET, JWT_ALGORITHM


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)  # Unauthorized

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except Exception as error:
            abort(401)  # Unauthorized

        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)  # Unauthorized

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        role = None

        try:
            user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            role = user.get('role', 'user')
        except Exception as error:
            abort(401)  # Unauthorized

        if role != 'admin':
            abort(403)  # Forbidden

        return func(*args, **kwargs)

    return wrapper
