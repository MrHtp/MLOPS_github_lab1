from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import numpy as np
import os

app = FastAPI(
    title="Iris Flower Prediction API (Dockerized)",
    description="Same API from my FastAPI lab, now running inside a Docker container.",
    version="2.0.0"
)

SPECIES_INFO = {
    0: {"name": "Setosa", "description": "Known for small size and wide sepals. Found in the Arctic."},
    1: {"name": "Versicolor", "description": "Also called Blue Flag. Native to North America, found near wetlands."},
    2: {"name": "Virginica", "description": "The largest species. Native to eastern North America with tall stems."}
}

MODEL_PATH = "iris_model.pkl"

def train_and_save_model():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)
    model = RandomForestClassifier(n_estimators=100, max_depth=4, random_state=42)
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    joblib.dump(model, MODEL_PATH)
    print(f"Model trained! Accuracy: {accuracy*100:.2f}%")
    return model, accuracy

if not os.path.exists(MODEL_PATH):
    model, accuracy = train_and_save_model()
else:
    model = joblib.load(MODEL_PATH)
    accuracy = model.score(*train_test_split(load_iris().data, load_iris().target, test_size=0.3, random_state=42)[1::2])

class IrisInput(BaseModel):
    sepal_length: float = Field(..., gt=0)
    sepal_width: float = Field(..., gt=0)
    petal_length: float = Field(..., gt=0)
    petal_width: float = Field(..., gt=0)

@app.get("/")
def health():
    return {"status": "healthy", "model": "Iris API v2.0", "container": "Docker"}

@app.post("/predict")
def predict(data: IrisInput):
    features = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model.predict(features)[0]
    confidence = round(float(max(model.predict_proba(features)[0])) * 100, 2)
    species = SPECIES_INFO[int(prediction)]
    return {
        "species_id": int(prediction),
        "species_name": species["name"],
        "confidence": confidence,
        "description": species["description"]
    }

@app.get("/model-info")
def model_info():
    return {"model": "RandomForest", "accuracy": round(accuracy * 100, 2), "n_estimators": 100, "container": "Docker"}

@app.get("/species")
def species():
    return {"species": SPECIES_INFO}
