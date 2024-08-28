import pytest
import allure
from src.movie_api.movie_api import MovieAPI
from src.movie_api.movie_models import MovieSearchResponse, MovieDetails, PopularMoviesResponse

movie_api = MovieAPI()

@allure.suite("Movie API Tests")
@allure.feature("Search Movies")
@allure.story("Search for movies by title")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("expected_title", [
    ("Inception"),
    ("The Matrix"),
    ("Interstellar")
])
def test_search_movie(expected_title):
    """Test searching for a movie by title."""
    # Make the API call and get the HTTP response
    response = movie_api.search_movie(expected_title)
    
    # Check status code
    with allure.step("Verify status code is 200"):
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Deserialize response JSON to a Pydantic model and validate schema
    with allure.step("Deserialize and validate response schema"):
        movie_search_response = MovieSearchResponse(**response.json())
        assert isinstance(movie_search_response, MovieSearchResponse), "Response is not of type MovieSearchResponse"

    # Verify specific data in the response
    with allure.step(f"Verify the first movie title is '{expected_title}'"):
        first_result = movie_search_response.results[0]
        assert first_result.title == expected_title, f"Expected title '{expected_title}', got {first_result.title}"

@allure.suite("Movie API Tests")
@allure.feature("Movie Details")
@allure.story("Get details for a specific movie")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("movie_id, expected_title", [
    (550, "Fight Club"),
    (13, "Forrest Gump"),
    (278, "The Shawshank Redemption")
])
def test_get_movie_details(movie_id, expected_title):
    """Test getting movie details by movie ID."""
    # Make the API call and get the HTTP response
    response = movie_api.get_movie_details(movie_id)
    
    # Check status code
    with allure.step("Verify status code is 200"):
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Deserialize response JSON to a Pydantic model and validate schema
    with allure.step("Deserialize and validate response schema"):
        movie_details = MovieDetails(**response.json())
        assert isinstance(movie_details, MovieDetails), "Response is not of type MovieDetails"

    # Verify specific data in the response
    with allure.step(f"Verify movie title is '{expected_title}'"):
        assert movie_details.title == expected_title, f"Expected title '{expected_title}', got {movie_details.title}"
        assert movie_details.id == movie_id, f"Expected movie ID {movie_id}, got {movie_details.id}"

@allure.suite("Movie API Tests")
@allure.feature("Popular Movies")
@allure.story("Get a list of popular movies")
@allure.severity(allure.severity_level.MINOR)
def test_get_popular_movies():
    """Test getting a list of popular movies."""
    # Make the API call and get the HTTP response
    response = movie_api.get_popular_movies()
    
    # Check status code
    with allure.step("Verify status code is 200"):
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Deserialize response JSON to a Pydantic model and validate schema
    with allure.step("Deserialize and validate response schema"):
        popular_movies_response = PopularMoviesResponse(**response.json())
        assert isinstance(popular_movies_response, PopularMoviesResponse), "Response is not of type PopularMoviesResponse"

    # Verify specific data in the response
    with allure.step("Verify the first movie has a title and vote_average"):
        first_result = popular_movies_response.results[0]
        assert 'title' in first_result.dict(), "Expected 'title' in the result, but it was missing"
        assert 'vote_average' in first_result.dict(), "Expected 'vote_average' in the result, but it was missing"
