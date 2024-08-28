# API Testing Framework

This is a Python-based API testing framework built using `pytest`, `Allure` for reporting, and design patterns like the Builder pattern. The framework is designed to test API endpoints in a structured, maintainable, and scalable way.

## Features

- **Modular Design**: Organized into separate modules for API clients, models, and builders.
- **Design Patterns**: Utilizes the Builder pattern to simplify the creation of complex request payloads.
- **Flexible Testing**: Supports parameterized tests to cover multiple scenarios.
- **Detailed Reporting**: Generates detailed test reports using Allure.

## Table of Contents

- [API Testing Framework](#api-testing-framework)
  - [Features](#features)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Set up environment variables:](#set-up-environment-variables)
  - [Setup](#setup)
  - [Directory Structure](#directory-structure)
- [Usage](#usage)
  - [Running Tests](#running-tests)
  - [Parameterized Tests](#parameterized-tests)
  - [Example Test Cases](#example-test-cases)
    - [Create a New List Using the Builder Pattern](#create-a-new-list-using-the-builder-pattern)
    - [Verify List Retrieval](#verify-list-retrieval)
- [Allure Reporting](#allure-reporting)
- [Extending the Framework](#extending-the-framework)
  - [Adding a New API Client](#adding-a-new-api-client)
  - [Adding New Tests](#adding-new-tests)
- [Contributing](#contributing)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/dasrodriguezs94/python-api-workshop.git
   cd api-testing-framework
   ```

Set up a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
Install the required packages:

```bash
pip install -r requirements.txt
```
## Set up environment variables:

Create a .env file in the root directory with the following content:

```bash
TMDB_BASE_URL=https://api.themoviedb.org/3
TMDB_API_KEY=your_api_key_here
TMDB_BEARER_TOKEN=your_bearer_token_here
```
## Setup
Ensure you have the following tools installed:

- Python 3.8+
- pytest: A testing framework.
- Allure: For generating detailed test reports.

To install additional tools for Allure reporting:

```bash
pip install allure-pytest
```
## Directory Structure
The framework is organized as follows:

```bash
.
├── src/
│   ├── base_api.py                # Base API client class
│   ├── list_api/
│   │   ├── list_api.py            # API client for List endpoints
│   │   └── list_models.py         # Pydantic models for list responses
│   └── movie_api/
│       └── movie_api.py           # API client for Movie endpoints
├── tests/
│   ├── test_list_api.py           # Test cases using the Builder pattern
│   ├── test_list_api.py           # Test cases for List API endpoints
│   └── conftest.py                # Fixtures and hooks
├── .env                           # Environment variables file
├── pytest.ini                     # Pytest configuration file
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```
# Usage
## Running Tests
To run all tests:

```bash
pytest -v --alluredir=allure-results
```
To run a specific test file:

```bash
pytest tests/<test_fiile>.py -v --alluredir=allure-results
```

## Parameterized Tests
This framework uses pytest's parameterization feature to run tests with multiple sets of inputs. 
Example:

```python
@pytest.mark.parametrize("movie_id, expected_title", [
    (550, "Fight Club"),
    (13, "Forrest Gump"),
    (278, "The Shawshank Redemption")
])
def test_get_movie_details(movie_id, expected_title):
    ...
```    
## Example Test Cases

### Create a New List Using the Builder Pattern
This test uses the Builder pattern to create a JSON payload for a new list:

```python
def test_create_list_with_builder():
    builder = ListBuilder().set_name("Marvel Movies").set_description("A list of Marvel franchise movies")
    payload = builder.build()

    response = list_api.create_list(payload['name'], payload['description'], payload['language'])
    assert response.status_code == 201
```

### Verify List Retrieval
``` python
def test_get_list():
    list_id = 12345
    response = list_api.get_list(list_id)
    assert response.status_code == 200
    ...
```

# Allure Reporting
To generate and view an Allure report:

1. Run the tests and generate the Allure results:

``` bash
pytest -v --alluredir=allure-results
```

2. Serve the Allure report:

```bash
allure serve allure-results
```
Docs at https://allurereport.org/docs/

# Extending the Framework
## Adding a New API Client
To add support for a new API, create a new module under src/:

1. Create a new directory, e.g., movie_api.
2. Add an API client class, e.g., MovieAPI.
3. Create corresponding models in the subdirectory.

## Adding New Tests
To add new tests, create a new file under tests/ and follow the existing structure. Use parameterization for different scenarios and the Builder pattern for complex payloads.

# Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit your changes (git commit -am 'Add your feature').
Push to the branch (git push origin feature/your-feature).
Create a new Pull Request.
License
This project is licensed under the MIT License. See the LICENSE file for details.