import os
import requests
import allure
from src.base_api import BaseAPI

class MovieAPI(BaseAPI):
    """API class for TMDb movie-related endpoints."""

    def __init__(self, base_url=None, api_key=None):
        base_url = base_url or os.getenv("TMDB_BASE_URL", "https://api.themoviedb.org/3")
        api_key = api_key or os.getenv("TMDB_API_KEY")
        super().__init__(base_url, api_key)

    @allure.step("Search for a movie by title")
    def search_movie(self, query: str) -> requests.Response:
        """Search for a movie by title."""
        endpoint = "search/movie"
        params = {"query": query}
        response = self.get(endpoint, params=params)
        return response

    @allure.step("Get details for a specific movie by ID")
    def get_movie_details(self, movie_id: int) -> requests.Response:
        """Get details for a specific movie by ID."""
        endpoint = f"movie/{movie_id}"
        response = self.get(endpoint)
        return response

    @allure.step("Get a list of popular movies")
    def get_popular_movies(self) -> requests.Response:
        """Get a list of popular movies."""
        endpoint = "movie/popular"
        response = self.get(endpoint)
        return response
