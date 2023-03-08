from unittest.mock import MagicMock
import pytest
from app.dao.director import DirectorDAO
from app.dao.models.director import Director
from app.service.director import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)
    director_1 = Director(id=1, name='Director_1')
    director_2 = Director(id=2, name='Director_2')

    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=[director_1, director_2])
    director_dao.create = MagicMock(return_value=3)
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()
    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        # assert director not is None
        assert isinstance(director, Director)
        assert director.id == 1

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert isinstance(directors, list)
        assert len(directors) == 2
        assert isinstance(directors[0], Director)

    def test_create(self):
        director_dict = {'id': 3, 'name': 'director_3'}
        director_id = self.director_service.create(director_dict)
        assert director_id == 3

    def test_update(self):
        director_dict = {'id': 3, 'name': 'director_3'}
        self.director_service.update(director_dict)

    def test_update_partial(self):
        director_dict = {'name': 'director_3'}
        self.director_service.update_partial(director_dict)

    def test_delete(self):
        self.director_service.delete(1)
