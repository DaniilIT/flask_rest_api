from unittest.mock import MagicMock
import pytest
from app.dao.genre import GenreDAO
from app.dao.models.genre import Genre
from app.service.genre import GenreService


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)
    genre_1 = Genre(id=1, name='Genre_1')
    genre_2 = Genre(id=2, name='Genre_2')

    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2])
    genre_dao.create = MagicMock(return_value=3)
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()
    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        # assert genre not is None
        assert isinstance(genre, Genre)
        assert genre.id == 1

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert isinstance(genres, list)
        assert len(genres) == 2
        assert isinstance(genres[0], Genre)

    def test_create(self):
        genre_dict = {'id': 3, 'name': 'genre_3'}
        genre_id = self.genre_service.create(genre_dict)
        assert genre_id == 3

    def test_update(self):
        genre_dict = {'id': 3, 'name': 'genre_3'}
        self.genre_service.update(genre_dict)

    def test_update_partial(self):
        genre_dict = {'name': 'genre_3'}
        self.genre_service.update_partial(genre_dict)

    def test_delete(self):
        self.genre_service.delete(1)
