import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from fastapi.testclient import TestClient
from main import app

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# --- Health Check Tests ---

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

# --- Predict Endpoint Tests ---

def test_predict_setosa():
    data = {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    result = response.json()
    assert result["species_name"] == "Setosa"
    assert result["confidence"] > 0
    assert "description" in result

def test_predict_versicolor():
    data = {"sepal_length": 5.9, "sepal_width": 3.0, "petal_length": 4.2, "petal_width": 1.5}
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    result = response.json()
    assert result["species_name"] == "Versicolor"

def test_predict_virginica():
    data = {"sepal_length": 6.3, "sepal_width": 3.3, "petal_length": 6.0, "petal_width": 2.5}
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    result = response.json()
    assert result["species_name"] == "Virginica"

def test_predict_has_confidence():
    data = {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}
    response = client.post("/predict", json=data)
    result = response.json()
    assert 0 < result["confidence"] <= 100

def test_predict_invalid_input():
    data = {"sepal_length": "abc", "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}
    response = client.post("/predict", json=data)
    assert response.status_code == 422

def test_predict_missing_field():
    data = {"sepal_length": 5.1, "sepal_width": 3.5}
    response = client.post("/predict", json=data)
    assert response.status_code == 422

# --- Model Info Tests ---

def test_model_info():
    response = client.get("/model-info")
    assert response.status_code == 200
    result = response.json()
    assert result["model_type"] == "Random Forest Classifier"
    assert result["accuracy"] > 0

# --- Species Info Tests ---

def test_species_list():
    response = client.get("/species")
    assert response.status_code == 200
    species = response.json()["species"]
    assert len(species) == 3
