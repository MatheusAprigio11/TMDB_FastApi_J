from typing import Optional
from pydantic import BaseModel


class Serie(BaseModel):
    id: Optional[int] = None
    name: str
    seasons: int
    year_start: int
    num_episodes: int
    status: str
    description: str
    vote_average: Optional[float]

