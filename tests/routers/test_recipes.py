from fastapi.testclient import TestClient
from app.main import app
from app.schemas import Recipe

client = TestClient(app)


def test_read_recipes():
    response = client.get("/recipes")
    assert response.status_code == 200


def test_read_recipe():
    recipe_id = 1
    response = client.get(f"/recipes/{recipe_id}")
    assert response.status_code == 200


def test_create_recipe():
    recipe = Recipe(
        title="Test Recipe",
        instructions="Prepare it like this.",
        ingredients=["onions", "chicken"],
    )
    response = client.post("/recipes/", json=recipe.model_dump())
    assert response.status_code == 201


def test_update_recipe():
    recipe_id = 1
    recipe = Recipe(
        title="Test Recipe",
        instructions="Prepare it like this.",
        ingredients=["onions", "chicken"],
    )
    response = client.put(f"/recipes/{recipe_id}", json=recipe.model_dump())
    assert response.status_code == 200


def test_delete_recipe():
    recipe_id = 1
    response = client.delete(f"/recipes/{recipe_id}")
    assert response.status_code == 200
