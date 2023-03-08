from unittest.mock import MagicMock

import pytest

from app.dao.models.movie import Movie
from app.dao.movie import MovieDAO
from app.service.movie import MovieService


@pytest.fixture()
def movie_dao():
    dao = MovieDAO(None)
    movie_1 = Movie(id=1, title='Movie_1', description='description',
                    trailer='trailer', year=2023, rating=4.3, genre_id=1, director_id=1)
    movie_2 = Movie(id=2, title='Movie_2', description='description',
                    trailer='trailer', year=2023, rating=4.3, genre_id=1, director_id=1)

    dao.get_one = MagicMock()
    dao.get_all = MagicMock(return_value=[movie_1, movie_2])
    dao.create = MagicMock(return_value=3)
    dao.update = MagicMock()
    dao.delete = MagicMock()
    return dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    parametres = [
        (1, {'id': 1, 'title': 'movie_1', 'description': 'description',
                      'trailer': 'trailer', 'year': 2023, 'rating': 4.3, 'genre_id': 1, 'director_id': 1}),
        (2, {'id': 2, 'title': 'movie_2', 'description': 'description',
             'trailer': 'trailer', 'year': 2023, 'rating': 4.3, 'genre_id': 1, 'director_id': 1}),
    ]

    @pytest.mark.parametrize('movie_id, movie', parametres)
    def test_get_one(self, movie_id, movie):
        self.movie_service.dao.get_one.return_value = movie
        assert self.movie_service.get_one(movie_id) == movie

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert isinstance(movies, list)
        assert len(movies) == 2
        assert isinstance(movies[0], Movie)

    def test_create(self):
        movie_dict = {'id': 3, 'title': 'movie_3', 'description': 'description',
                      'trailer': 'trailer', 'year': 2023, 'rating': 4.3, 'genre_id': 1, 'director_id': 1}
        movie_id = self.movie_service.create(movie_dict)
        assert movie_id == 3

    def test_update(self):
        movie_dict = {'id': 3, 'title': 'movie_3', 'description': 'description',
                      'trailer': 'trailer', 'year': 2023, 'rating': 4.3, 'genre_id': 1, 'director_id': 1}
        self.movie_service.update(movie_dict)

    def test_update_partial(self):
        movie_dict = {'title': 'movie_3'}
        self.movie_service.update_partial(movie_dict)

    def test_delete(self):
        self.movie_service.delete(1)
