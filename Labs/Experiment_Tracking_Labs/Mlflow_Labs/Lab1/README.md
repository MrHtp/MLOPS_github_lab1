# MLflow Lab – Iris Classification Experiment Tracking

## How It Connects to My Other Labs

This lab adds **experiment tracking** to the same Iris flower prediction pipeline built across all previous labs:

- **Lab 1 (GitHub Actions)** – automated testing for the Iris pipeline
- **Lab 2 (FastAPI)** – served the Random Forest model as a REST API
- **Lab 4 (MLMD)** – tracked metadata and lineage of the Iris pipeline
- **Lab 5 (Docker)** – containerized the FastAPI prediction service
- **This Lab (MLflow)** – tracks and compares multiple model experiments before deciding which model to deploy

MLflow answers the question: *"Which model should go into the FastAPI + Docker pipeline?"*

---

## What This Lab Does

Runs three classification models on the Iris dataset and logs every experiment to MLflow:

| Model | Key Parameters |
|---|---|
| Logistic Regression | C=1.0, max_iter=200 |
| Random Forest | n_estimators=100, max_depth=5 |
| SVM | kernel=rbf, C=1.0 |

Each run logs:
- **Parameters** – hyperparameters used
- **Metrics** – accuracy, F1 score, precision, recall
- **Model artifact** – saved and registered in MLflow Model Registry
- **Tags** – dataset name, model type

---

## How to Run It

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run experiments
```bash
python iris_experiment.py
```

### 3. Launch MLflow UI
```bash
mlflow ui
```

### 4. Open the dashboard
```
http://localhost:5000
```

You will see the `Iris_Classification_Experiments` experiment with 3 runs — compare metrics, parameters, and artifacts side by side.

---

## What the MLflow UI Shows

- **Experiment view** – all 3 runs listed with their accuracy and F1 scores
- **Run comparison** – select any two runs to compare parameters and metrics side by side
- **Model Registry** – each model is registered as `Iris_Logistic_Regression`, `Iris_Random_Forest`, and `Iris_SVM`
- **Artifacts** – saved model files ready for serving

---

## Results

All three models perform well on the Iris dataset. Random Forest and SVM typically achieve the highest accuracy (~97%), which is consistent with the model deployed in the FastAPI lab.
