from pydantic import BaseModel
from typing import List, Optional

# Define a Pydantic model for the movie search result
class MovieSearchResult(BaseModel):
    id: int
    title: str
    overview: Optional[str]
    release_date: Optional[str]
    vote_average: Optional[float]
    vote_count: Optional[int]

# Define a Pydantic model for the movie details response
class MovieDetails(MovieSearchResult):
    budget: Optional[int]
    revenue: Optional[int]

# Define a Pydantic model for the movie search response
class MovieSearchResponse(BaseModel):
    results: List[MovieSearchResult]
    total_results: int
    total_pages: int

# Define a Pydantic model for popular movies response
class PopularMoviesResponse(BaseModel):
    results: List[MovieSearchResult]
    page: int
    total_results: int
    total_pages: int