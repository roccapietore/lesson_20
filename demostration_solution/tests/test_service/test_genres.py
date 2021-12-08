import pytest
from unittest.mock import MagicMock

from dao.genre import DirectorDAO
from dao.model.genre import Genre
from service.genre import GenreService


@pytest.fixture()
def genre_dao():
    genre_dao = DirectorDAO(None)
    drama = Genre(id=1, name="drama")
    horror = Genre(id=2, name="horror")
    comedy = Genre(id=3, name="comedy")

    genre_dao.get_one = MagicMock(return_value=drama)
    genre_dao.get_all = MagicMock(return_value=[drama, horror, comedy])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.update = MagicMock()
    genre_dao.partially_update = MagicMock()
    genre_dao.delete = MagicMock()
    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        new_genre = {

            "name": "detective"
        }
        genre = self.genre_service.create(new_genre)
        assert genre.id is not None

    def test_update(self):
        genre_ = {
            "id": "2",
            "name": "detective"
        }
        genre = self.genre_service.update(genre_)
        assert genre.id is not None

    def test_partially_update(self):

        genre_ = {
            "id": "1",
            "name": "detective"
        }
        genre = self.genre_service.partially_update(genre_)
        assert genre.id is not None

    def test_delete(self):
        self.genre_service.delete(1)
