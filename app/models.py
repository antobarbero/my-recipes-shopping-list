from typing import Optional
from uuid import uuid4
from pydantic import BaseModel, Field


class Recipe(BaseModel):
    id: str = Field(default_factory=uuid4, alias="_id")
    title: str
    instructions: str
    ingredients: list[str]

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "Chicken with onions",
                "instructions": "Cook the onions with the chicken.",
                "ingredients": ["onions", "chicken"],
            }
        }


class RecipeUpdate(BaseModel):
    title: Optional[str]
    instructions: Optional[str]
    ingredients: Optional[list[str]]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Chicken with onions",
                "instructions": "Cook the onions with the chicken.",
                "ingredients": "['onions', 'chicken']",
            }
        }
