from pydantic import BaseModel


class Directors(BaseModel):
    name: str


class Films(BaseModel):
    name: str
    director_id: int