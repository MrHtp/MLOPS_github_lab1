# Docker Lab - Dockerized Iris Prediction API

Hrishikesh Prabhu | IE-7374 MLOps | Spring 2026

## What This Lab Is About

This lab takes the Iris Prediction API I built in my FastAPI lab and packages it into a Docker container. The idea is simple — instead of asking someone to install Python, create a virtual environment, install dependencies, train the model, and then run the server, they can just run one command and everything works.

## What I Changed From the Original

The original Docker lab just trains a model inside a container and prints "model training successful." I replaced that with something more useful — my actual FastAPI prediction API running inside Docker. It includes confidence scores, species descriptions, and all four endpoints from my FastAPI lab.

## How It Connects to My Other Labs

- **GitHub Lab 1** — learned CI/CD and testing
- **FastAPI Lab** — built the Iris API with confidence scores and species info
- **MLMD Lab** — tracked that pipeline's metadata
- **This Lab** — containerized the same API so it can run anywhere

## What's Inside the Container

The Docker container packages everything needed to run the API: Python 3.10, scikit-learn, FastAPI, uvicorn, and the model training code. When the container starts, it automatically trains the Random Forest model and starts serving predictions.

**Endpoints:**
- `GET /` — health check (confirms it's running in Docker)
- `POST /predict` — send flower measurements, get species + confidence
- `GET /model-info` — shows model type, accuracy, and that it's running in Docker
- `GET /species` — lists all three Iris species with descriptions

## How to Run It

1. Make sure Docker is installed and running

2. Navigate to the lab
```bash
cd Labs/Docker_Labs/Lab1
```

3. Build the image
```bash
docker build -t iris-api .
```

4. Run the container
```bash
docker run -d -p 8000:8000 --name iris-container iris-api
```

5. Open http://localhost:8000/docs and test the API

6. When done, stop the container
```bash
docker stop iris-container
docker rm iris-container
```

## What I Learned

- Docker makes deployment way easier — no more "it works on my machine" problems
- The Dockerfile is basically a recipe: start with Python, copy your code, install dependencies, run the server
- Using `python:3.10-slim` instead of the full image keeps the container small
- The container trains the model on startup, so it's completely self-contained
- Exposing port 8000 lets you access the API from your browser just like running it locally