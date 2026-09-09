from pydantic import BaseModel

class MovieRequest(BaseModel):
    title: str
    top_n = 5