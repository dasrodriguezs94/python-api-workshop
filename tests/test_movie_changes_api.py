from src.changes_api.changes_api import ChangesAPI
from src.changes_api.changes_models import ChangesMoviesResponse


changes_api = ChangesAPI()

def test_get_changes_of_movies():
    response = changes_api.movie_list_change()
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    movie_change_response = ChangesMoviesResponse(**response.json())

    assert isinstance(movie_change_response, ChangesMoviesResponse), "Response is not of type ChangesMoviesResponse"

    assert len(movie_change_response.results) == 100, f"Expected 100 items in the response but got {len(movie_change_response.results)}"