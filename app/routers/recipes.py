from fastapi import APIRouter, status
from app.models import Recipe, RecipeUpdate
from typing import List
from fastapi import Body, Request, Response, HTTPException
from fastapi.encoders import jsonable_encoder

router = APIRouter(prefix="/recipes")


@router.get("/", response_description="List all recipes", response_model=List[Recipe])
def read_recipes(request: Request):
    """Retrieves all recipes ids and titles."""
    recipes = list(request.app.database["recipes"].find(limit=100))
    return recipes


@router.post(
    "/",
    response_description="Create a new recipe.",
    status_code=status.HTTP_201_CREATED,
    response_model=Recipe,
)
def create_recipe(request: Request, recipe: Recipe = Body(...)):
    """Updates recipe with the given `recipe_id`."""
    recipe = jsonable_encoder(recipe)
    new_recipe = request.app.database["recipes"].insert_one(recipe)
    created_recipe = request.app.database["recipes"].find_one(
        {"_id": new_recipe.inserted_id}
    )

    return created_recipe


@router.get(
    "/{recipe_id}",
    response_description="Get a single recipe by id",
    response_model=Recipe,
)
def read_recipe(recipe_id: str, request: Request):
    """Retrieves recipe with the given `recipe_id`."""
    if (
        recipe := request.app.database["recipes"].find_one({"_id": recipe_id})
    ) is not None:
        return recipe
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Recipe with ID {recipe_id} not found",
    )


@router.put(
    "/{recipe_id}", response_description="Update a recipe.", response_model=Recipe
)
def update_recipe(recipe_id: str, request: Request, recipe: RecipeUpdate = Body(...)):
    """Updates recipe with the given `recipe_id`."""
    recipe_dict = {k: v for k, v in recipe.model_dump() if v is not None}
    if len(recipe_dict) >= 1:
        update_result = request.app.database["recipes"].update_one(
            {"_id": recipe_id}, {"$set": recipe}
        )

        if update_result.modified_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Recipe with ID {recipe_id} not found.",
            )

    if (
        existing_recipe := request.app.database["recipes"].find_one({"_id": recipe_id})
    ) is not None:
        return existing_recipe

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Recipe with ID {recipe_id} not found.",
    )


@router.delete("/{recipe_id}", response_description="Delete a recipe.")
def delete_recipe(recipe_id: str, request: Request, response: Response):
    """Deletes recipe with the given `recipe_id`."""
    delete_result = request.app.database["recipes"].delete_one({"_id": recipe_id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Recipe with ID {recipe_id} not found",
    )
