import os
import requests
import allure
from src.base_api import BaseAPI

class ChangesAPI(BaseAPI):
    """API class for list-related endpoints."""

    def __init__(self, base_url=None, bearer_token=None):
        base_url = base_url or os.getenv("TMDB_BASE_URL", "https://api.themoviedb.org/3")
        bearer_token = bearer_token or os.getenv("TMDB_BEARER_TOKEN")
        super().__init__(base_url)
        self.session.headers.update({
            "Authorization": f"Bearer {bearer_token}"
        })

    @allure.step("Get recent movie changes")
    def movie_list_change(self, end_date: str = None, page: str = None, start_date: str = None) -> requests.Response:
        """Get recent movie changes list"""
        endpoint = "movie/changes"
        response = self.get(endpoint)
        return response
    