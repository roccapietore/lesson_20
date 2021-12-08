import pytest
from unittest.mock import MagicMock

from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)
    movie_1 = Movie(id=1, title="smth", description ="smth", trailer="smth",
                    year="smth", rating="smth", genre_id="smth", director_id="smth")
    movie_2 = Movie(id=2, title="smth", description ="smth", trailer="smth",
                    year="smth", rating="smth", genre_id="smth", director_id="smth")
    movie_3 = Movie(id=3, title="smth", description ="smth", trailer="smth",
                    year="smth", rating="smth", genre_id="smth", director_id="smth")

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.update = MagicMock()
    movie_dao.partially_update = MagicMock()
    movie_dao.delete = MagicMock()
    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        new_movie = {
            "title": "smth", "description": "smth",  "trailer": "smth",
            "year": "smth", "rating": "smth", "genre_id": "smth", "director_id": "smth"
        }
        movie = self.movie_service.create(new_movie)
        assert movie.id is not None

    def test_update(self):
        movie_ = {
            "title": "smth", "description": "smth", "trailer": "smth",
            "year": "smth", "rating": "smth", "genre_id": "smth", "director_id": "smth"
        }
        movie = self.movie_service.update(movie_)
        assert movie.id is not None

    def test_partially_update(self):
        movie_ = {
            "id": "1", "title": "smth", "description": "smth", "trailer": "smth",
            "year": "smth", "rating": "smth", "genre_id": "smth", "director_id": "smth"
        }
        movie = self.movie_service.partially_update(movie_)
        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)
