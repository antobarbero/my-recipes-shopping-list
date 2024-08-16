from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Recipe(BaseModel):
    title: str
    instructions: str
    ingredients: List[str]


@app.get("/")
def read_root():
    return "Welcome to the recipes web api."


@app.get("/recipes")
def read_recipes():
    """Retrieves all recipes ids and titles."""
    # ToDo: implement.
    return "Not implemented"


@app.get("/recipes/{recipe_id}")
def read_recipe(recipe_id: int):
    """Retrieves recipe with the given `recipe_id`."""
    # ToDo: implement.
    return {
        "recipe_id": recipe_id,
        "instructions": "Prepare",
        "ingredients": "chicken, wine and onions",
    }


@app.put("/recipes/{recipe_id}")
def update_recipe(recipe_id: int, recipe: Recipe):
    """Updates recipe with the given `recipe_id`."""
    # ToDo: implement.
    return {"recipe_title": recipe.title, "recipe_id": recipe_id}


@app.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int):
    """Deletes recipe with the given `recipe_id`."""
    # ToDo: implement.
    return {"recipe_id": recipe_id}
