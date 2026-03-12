# MLMD Lab - Tracking the Iris Prediction Pipeline

Hrishikesh Prabhu | IE-7374 MLOps | Spring 2026

## What This Lab Is About

In real ML projects, you don't just train a model and forget about it. You need to know things like — what data was used to train the model? Which version of the model is currently running in production? What changed between version 1 and version 2?

That's what ML Metadata does. It keeps track of everything that happens in your pipeline so you can trace back and answer these questions later.

## Why I Built My Own Metadata Store

The original lab uses Google's ml-metadata library with TFDV. But TFDV doesn't work on Mac (Python 3.13 compatibility issues), and ml-metadata itself had problems too. Instead of fighting with dependencies, I decided to build my own metadata store from scratch using SQLite.

Turns out this was actually a better learning experience — I had to understand what artifact types, execution types, events, and contexts actually mean instead of just calling someone else's API.

## How This Connects to My Other Labs

This isn't a standalone lab. I'm tracking the same Iris prediction pipeline I built in my previous labs:

- In the **GitHub Lab**, I learned how to test code and set up CI/CD
- In the **FastAPI Lab**, I built an actual API that serves predictions with confidence scores and species descriptions
- In **this lab**, I'm recording metadata for that same pipeline — so I can trace from the deployed API all the way back to the original training dataset

## What Gets Tracked

**Things the pipeline creates (artifacts):**
- The Iris training dataset (105 samples, 4 features)
- A custom schema I generated using pandas (data types, stats, null checks)
- The trained Random Forest model (97%+ accuracy)
- The FastAPI deployment config (4 endpoints including /predict with confidence)

**Steps the pipeline runs (executions):**
- Data validation — reads the dataset and creates a schema
- Model training — trains Random Forest, measures accuracy and confidence
- API deployment — deploys the model behind FastAPI

**The cool part** is lineage tracking. I can start from the API and trace backwards: this API serves this model, which was trained on this dataset. If something breaks in production, I know exactly where to look.

## How to Run It

1. Navigate to the lab
```bash
cd Labs/MLMD_Labs/Lab1
```

2. Set up the environment
```bash
python3 -m venv mlmd_env
source mlmd_env/bin/activate
pip install pandas numpy scikit-learn joblib jupyter ipykernel
python -m ipykernel install --user --name=mlmd_env --display-name="MLMD Env"
```

3. Open and run the notebook
```bash
jupyter notebook MLMD_Custom_Lab.ipynb
```
Select "MLMD Env" as the kernel and hit Run All.

## What I Took Away From This

The biggest thing I learned is that metadata tracking isn't just bookkeeping — it's how you debug production ML systems. When a model starts giving bad predictions, you need to know what data it was trained on and what changed. Without metadata, you're basically guessing.

Building my own store also helped me see that the core idea is pretty simple — you're just recording relationships between inputs, processes, and outputs. The SQLite implementation is like 80 lines of code but it covers all the key concepts from the MLMD library.