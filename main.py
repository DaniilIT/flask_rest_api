from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from app.views.movie import movie_ns
from app.views.director import director_ns
from app.views.genre import genre_ns


def create_app(config_object):
    application = Flask(__name__, )
    application.config.from_object(config_object)
    application.app_context().push()
    register_extensions(application)
    return application


def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 2}
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    app.run(host="localhost", port=5000)
