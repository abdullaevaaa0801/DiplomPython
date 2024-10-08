import requests
from tests.constants import API_base_url
from tests.conftest import token


class ApiKinopoisk:
    """
    Базовый класс для АПИ кинопоиск
    """

    def __init__(self):
        """Инициализация и запуск АПИ, содержит токен и базовый url """
        self.base_url = API_base_url
        self.headers = token

    def get_anime_top250(self, list='top250', tipe='anime'):
        params = {
            "lists": list,
            "type": tipe
        }
        response = requests.get(f"{self.base_url}/movie", headers=self.headers, params=params)
        return response
    
    def find_by_name_actor(self, name="Джонни Дэпп", page=1, limit=1):
        params = {
            "page": page,
            "limit": limit,
            "query": name
        }
        response = requests.get(f"{self.base_url}/person/search", headers=self.headers, params=params)
        return response

    def get_film_by_name(self, name="Один дома", page=1, limit=1):
        params = {
            "page": page,
            "limit": limit,
            "query": name
        }
        response = requests.get(f"{self.base_url}//movie/search", headers=self.headers, params=params)
        return response

    def find_by_nomination_title(self, nomination="Oscar", page=1, limit=10, year=2021):
        params = {
            "page": page,
            "limit": limit,
            "nomination.awards.title": nomination,
            "nomination.awards.year": year
        }
        response = requests.get(f"{self.base_url}/person/awards", headers=self.headers, params=params)
        return response

    def get_random_title_with_rating(self, min_rating=8, age_rating=18):
        params = {
            "rating.kp": min_rating,
            "ageRating": age_rating
        }
        response = requests.get(f"{self.base_url}/movie/random", headers=self.headers, params=params)
        return response
