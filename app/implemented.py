# container

from setup_db import db
from .dao.movie import MovieDao
from .service.movie import MovieService
from .dao.director import DirectorDao
from .service.director import DirectorService
from .dao.genre import GenreDao
from .service.genre import GenreService


movie_dao = MovieDao(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDao(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDao(db.session)
genre_service = GenreService(genre_dao)
