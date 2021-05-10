import pytest
from pathlib import Path
from app import app


@pytest.fixture
def client():
    BASE_DIR = Path(__file__).resolve().parent.parent
    app.config["TESTING"] = True

    yield app.test_client()  # tests run here


def test_add_image(client):
    """Test upload of image"""
    response = client.get("/add",  body={"filename": "cars.jpg"})
    assert response.status_code == 200


def test_delete_image(client):
    """Test deletion of image"""
    response = client.get("/delete",  body={"filename": "cars.jpg"})
    assert response.status_code == 200


def test_search_getall(client):
    """Featch all images in repository"""
    response = client.get("/search")
    assert response.status_code == 200
    assert response.json[0]['filename'] == "cars.jpg"
    assert response.json[1]['filename'] == "dog.jpg"
    assert response.json[2]['filename'] == "sunrise.jpg"


def test_search_from_filename(client):
    """Ensure search from filename is correct"""
    response = client.get(
        "/search",  params={"filename": "cars.jpg"}, content_type="html/text")
    assert response.status_code == 200
    assert response.json[0]['filename'] == "cars.jpg"
