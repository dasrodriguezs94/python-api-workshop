from pydantic import BaseModel, Field
from typing import List, Optional

class CreateListResponse(BaseModel):
    """Model representing the response after creating a list."""
    status_message: str
    success: bool
    status_code: int
    list_id: int

class ListItem(BaseModel):
    """Model representing an item in the list."""
    adult: bool
    backdrop_path: Optional[str]
    genre_ids: List[int]
    id: int
    media_type: str
    original_language: str
    original_title: Optional[str]
    overview: Optional[str]
    popularity: float
    poster_path: Optional[str]
    release_date: Optional[str]
    title: Optional[str]
    video: bool
    vote_average: float
    vote_count: int

class GetListResponse(BaseModel):
    """Model representing the response when retrieving a list by ID."""
    created_by: str
    description: str
    favorite_count: int
    id: int
    items: List[ListItem]
    item_count: int
    iso_639_1: str
    name: str
    poster_path: Optional[str]

class DeleteListResponse(BaseModel):
    """Model representing the response after deleting a list."""
    status_code: int
    status_message: str
