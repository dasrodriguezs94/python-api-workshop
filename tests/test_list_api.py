import pytest
import allure
from src.list_api.list_api import ListAPI
from src.list_api.list_models import CreateListResponse, GetListResponse, DeleteListResponse

# Initialize the ListAPI instance directly in the test module

list_api = ListAPI()

@allure.suite("List API Tests")
@allure.feature("Create List")
def test_create_list():
    """Test creating a new list."""
    response = list_api.create_list("My Favorite Movies", "A list of my all-time favorite movies.")
    assert response.status_code == 200, f"Expected status code 201, got {response.status_code}"

    # Deserialize response and validate schema
    create_list_response = CreateListResponse(**response.json())
    assert create_list_response.success is True
    assert create_list_response.status_code == 1
    assert create_list_response.list_id is not None

@allure.suite("List API Tests")
@allure.feature("Get List")
def test_get_list():
    """Test retrieving a list by ID."""
    # First, create a list
    create_response = list_api.create_list("Marvel Movies", "A list of Marvel franchise movies.")
    list_id = create_response.json()["list_id"]

    # Now, retrieve the list by ID
    response = list_api.get_list(list_id)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    # Deserialize response and validate schema
    get_list_response = GetListResponse(**response.json())
    assert isinstance(get_list_response, GetListResponse)
    assert get_list_response.id == list_id
    assert get_list_response.name == "Marvel Movies"
    assert isinstance(get_list_response.items, list)
    assert len(get_list_response.items) >= 0  # Ensure items is a list and can be empty

@allure.suite("List API Tests")
@allure.feature("Delete List")
def test_delete_list():
    """Test deleting a list by ID."""
    # First, create a list
    create_response = list_api.create_list("Temporary List", "This list will be deleted.")
    list_id = create_response.json()["list_id"]

    # Now, delete the list by ID
    response = list_api.delete_list(list_id)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    # Deserialize response and validate schema
    delete_list_response = DeleteListResponse(**response.json())
    assert delete_list_response.status_code == 13
    assert delete_list_response.status_message == "The item/record was deleted successfully."

    # Verify that the list no longer exists
    get_response = list_api.get_list(list_id)
    assert get_response.status_code == 404, f"Expected status code 404, got {get_response.status_code}"