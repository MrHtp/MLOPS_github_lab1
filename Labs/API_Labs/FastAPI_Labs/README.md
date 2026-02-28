# FastAPI Lab - Iris Flower Prediction API

Hrishikesh Prabhu | IE-7374 MLOps | Spring 2026

## About This Lab

This lab is about serving a machine learning model as a REST API using FastAPI and uvicorn. The idea is to train a model, save it, and then let users send flower measurements through an API to get predictions back.

I started with the base lab that used a Decision Tree, but made several changes to make it my own.

## What I Changed From the Original

- **Switched from Decision Tree to Random Forest** — gives better accuracy (97.78% vs the original)
- **Added confidence scores** — the API now tells you how confident the model is in its prediction
- **Returns species name and description** — instead of just returning a number like 0 or 1, it returns "Setosa" along with a fun description of the flower
- **Added a `/model-info` endpoint** — shows what model is being used, its accuracy, and what features it expects
- **Added a `/species` endpoint** — lists all three Iris species with descriptions
- **Added API tests using pytest** — 9 test cases that check all endpoints, building on what I learned in GitHub Lab 1

## How It Connects to GitHub Lab 1

In Lab 1 I learned pytest and GitHub Actions for testing simple Python functions. Here I applied those same testing concepts to test API endpoints using FastAPI's TestClient. Same idea — write tests, run them automatically, catch bugs early.

## API Endpoints

| Method | Endpoint | What It Does |
|---|---|---|
| GET | `/` | Health check — tells you the API is running |
| POST | `/predict` | Send flower measurements, get species prediction with confidence |
| GET | `/model-info` | Shows model type, accuracy, and features |
| GET | `/species` | Lists all three Iris species with descriptions |

## Sample Predict Response

```json
{
    "species_id": 0,
    "species_name": "Setosa",
    "confidence": 100.0,
    "description": "Iris Setosa is known for its small size and wide sepals..."
}
```

## Project Structure

```
FastAPI_Labs/
├── model/
│   ├── iris_model.pkl          # trained Random Forest model
│   └── model_metadata.json     # model info (type, accuracy, features)
├── src/
│   ├── __init__.py
│   ├── data.py                 # loads and splits the Iris dataset
│   ├── train.py                # trains Random Forest and saves model + metadata
│   ├── predict.py              # loads model and makes predictions with confidence
│   ├── main.py                 # FastAPI app with all endpoints
│   └── test_api.py             # 9 pytest tests for all endpoints
├── assets/
├── README.md
└── requirements.txt
```

## How to Run It Yourself

1. Clone and navigate to the lab
```bash
git clone https://github.com/MrHtp/MLOPS_github_lab1.git
cd MLOPS_github_lab1/Labs/API_Labs/FastAPI_Labs
```

2. Create and activate virtual environment
```bash
python3 -m venv fastapi_env
source fastapi_env/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
pip install pytest
```

4. Train the model
```bash
cd src
python3 train.py
```
You should see "Model Accuracy: 97.78%"

5. Run the tests
```bash
pytest test_api.py -v
```
All 9 tests should pass.

6. Start the API server
```bash
uvicorn main:app --reload
```

7. Open your browser and go to http://127.0.0.1:8000/docs to interact with the API.

## What I Learned

- How to serve ML models as APIs using FastAPI — its auto-generated docs at /docs are really useful
- Pydantic models for request/response validation — catches bad input automatically
- How Random Forest's predict_proba gives you confidence scores which Decision Trees don't do as well
- Testing APIs with FastAPI's TestClient — way easier than I expected
- The connection between model training and model serving — train once, serve many times