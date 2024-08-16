from fastapi import APIRouter
from typing import List

from pydantic import BaseModel

router = APIRouter(prefix="/recipes")


class Recipe(BaseModel):
    title: str
    instructions: str
    ingredients: List[str]


@router.get("/")
def read_recipes():
    """Retrieves all recipes ids and titles."""
    # ToDo: implement.
    return "Not implemented"


@router.post("/", status_code=201)
def create_recipe(recipe: Recipe):
    """Updates recipe with the given `recipe_id`."""
    # ToDo: implement.
    return {"recipe_title": recipe.title}


@router.get("/{recipe_id}")
def read_recipe(recipe_id: int):
    """Retrieves recipe with the given `recipe_id`."""
    # ToDo: implement.
    return {
        "recipe_id": recipe_id,
        "instructions": "Prepare",
        "ingredients": "chicken, wine and onions",
    }


@router.put("/{recipe_id}")
def update_recipe(recipe_id: int, recipe: Recipe):
    """Updates recipe with the given `recipe_id`."""
    # ToDo: implement.
    return {"recipe_title": recipe.title, "recipe_id": recipe_id}


@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: int):
    """Deletes recipe with the given `recipe_id`."""
    # ToDo: implement.
    return {"recipe_id": recipe_id}
