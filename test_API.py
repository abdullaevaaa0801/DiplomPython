from Pages.page_api import ApiKinopoisk


api_kinopoisk = ApiKinopoisk()


def test_anime_top250():
    response = api_kinopoisk.get_anime_top250()
    assert response.status_code == 200


def test_search_person():
    response = api_kinopoisk.find_by_name_actor()
    assert response.status_code == 200


def test_search_movie_name():
    response = api_kinopoisk.get_film_by_name()
    assert response.status_code == 200


def test_search_awards():
    response = api_kinopoisk.find_by_nomination_title()
    assert response.status_code == 200


def test_search_random_movie():
    response = api_kinopoisk.get_random_title_with_rating()
    assert response.status_code == 200
