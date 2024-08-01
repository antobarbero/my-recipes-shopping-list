from fastapi.testclient import TestClient
from app.main import app, Item

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_item():
    item_id = 1
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"item_id": item_id, "q": None}

    response = client.get(f"/items/{item_id}", params={"q": "test"})
    assert response.status_code == 200
    assert response.json() == {"item_id": item_id, "q": "test"}


def test_update_item():
    item_id = 1
    item = Item(name="Test Item", price=10.5, is_offer=True)
    response = client.put(f"/items/{item_id}", json=item.dict())
    assert response.status_code == 200
    assert response.json() == {"item_name": item.name, "item_id": item_id}
