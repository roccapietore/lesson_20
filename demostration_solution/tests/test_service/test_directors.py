import pytest
from unittest.mock import MagicMock

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)
    director_1 = Director(id=1, name="Director_1")
    director_2 = Director(id=2, name="Director_2")
    director_3 = Director(id=3, name="Director_3")

    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=[director_1, director_2, director_3])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.update = MagicMock()
    director_dao.partially_update = MagicMock()
    director_dao.delete = MagicMock()
    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_create(self):
        new_director = {
            "name": "director"
        }
        director = self.director_service.create(new_director)
        assert director.id is not None

    def test_update(self):
        director_ = {
            "id": "2",
            "name": "director"
        }
        director = self.director_service.update(director_)
        assert director.id is not None

    def test_partially_update(self):

        director_ = {
            "id": "1",
            "name": "detective"
        }
        director = self.director_service.partially_update(director_)
        assert director.id is not None

    def test_delete(self):
        self.director_service.delete(1)
