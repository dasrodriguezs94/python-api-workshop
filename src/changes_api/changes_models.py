from pydantic import BaseModel, Field
from typing import List, Optional

class ChangesMoviesResponse(BaseModel):
    """Model representing the response after creating a list."""
    results: list
    page: int
    total_pages: int
    total_results: int