import os
import requests
import allure
from src.base_api import BaseAPI

class ListAPI(BaseAPI):
    """API class for list-related endpoints."""

    def __init__(self, base_url=None, bearer_token=None):
        base_url = base_url or os.getenv("TMDB_BASE_URL", "https://api.themoviedb.org/3")
        bearer_token = bearer_token or os.getenv("TMDB_BEARER_TOKEN")
        super().__init__(base_url)
        self.session.headers.update({
            "Authorization": f"Bearer {bearer_token}"
        })

    @allure.step("Create a new list")
    def create_list(self, name: str, description: str) -> requests.Response:
        """Create a new list."""
        endpoint = "list"
        json_data = {
            "name": name,
            "description": description
        }
        response = self.post(endpoint, json=json_data)
        return response

    @allure.step("Get a list by ID")
    def get_list(self, list_id: int) -> requests.Response:
        """Get a list by ID."""
        endpoint = f"list/{list_id}"
        response = self.get(endpoint)
        return response

    @allure.step("Delete a list by ID")
    def delete_list(self, list_id: int) -> requests.Response:
        """Delete a list by ID."""
        endpoint = f"list/{list_id}"
        response = self.delete(endpoint)
        return response
