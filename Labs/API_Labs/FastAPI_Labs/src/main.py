from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, Field
from predict import predict_data, predict_with_confidence
import json
import os

app = FastAPI(
    title="Iris Flower Prediction API",
    description="A Random Forest based API to predict Iris flower species with confidence scores.",
    version="2.0.0"
)

# Species info dictionary
SPECIES_INFO = {
    0: {
        "name": "Setosa",
        "description": "Iris Setosa is known for its small size and wide sepals. It is commonly found in the Arctic and is the easiest species to distinguish from the other two."
    },
    1: {
        "name": "Versicolor",
        "description": "Iris Versicolor, also known as the Blue Flag, is native to North America. It has medium-sized petals and is often found near wetlands and streams."
    },
    2: {
        "name": "Virginica",
        "description": "Iris Virginica is the largest of the three species. It is native to eastern North America and is known for its tall stems and large flowers."
    }
}

# --- Pydantic Models ---

class IrisData(BaseModel):
    sepal_length: float = Field(..., gt=0, description="Sepal length in cm")
    sepal_width: float = Field(..., gt=0, description="Sepal width in cm")
    petal_length: float = Field(..., gt=0, description="Petal length in cm")
    petal_width: float = Field(..., gt=0, description="Petal width in cm")

class IrisResponse(BaseModel):
    species_id: int
    species_name: str
    confidence: float
    description: str

class ModelInfoResponse(BaseModel):
    model_type: str
    accuracy: float
    features: list
    classes: list

# --- Endpoints ---

@app.get("/", status_code=status.HTTP_200_OK)
async def health_ping():
    """Health check endpoint to verify the API is running."""
    return {"status": "healthy", "model": "Iris Prediction API v2.0"}

@app.post("/predict", response_model=IrisResponse)
async def predict_iris(iris_features: IrisData):
    """Predict the Iris species with confidence score and description."""
    try:
        features = [[iris_features.sepal_length, iris_features.sepal_width,
                      iris_features.petal_length, iris_features.petal_width]]

        prediction, confidence = predict_with_confidence(features)
        species_id = int(prediction[0])
        species = SPECIES_INFO[species_id]

        return IrisResponse(
            species_id=species_id,
            species_name=species["name"],
            confidence=round(confidence * 100, 2),
            description=species["description"]
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/model-info", response_model=ModelInfoResponse)
async def model_info():
    """Returns information about the trained model."""
    try:
        metadata_path = os.path.join(os.path.dirname(__file__), "..", "model", "model_metadata.json")
        with open(metadata_path, "r") as f:
            metadata = json.load(f)
        return ModelInfoResponse(**metadata)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Model metadata not found. Please train the model first.")

@app.get("/species", status_code=status.HTTP_200_OK)
async def get_species():
    """Returns information about all Iris species."""
    return {"species": SPECIES_INFO}