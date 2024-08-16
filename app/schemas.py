from typing import List

from pydantic import BaseModel


class Recipe(BaseModel):
    title: str
    instructions: str
    ingredients: List[str]
