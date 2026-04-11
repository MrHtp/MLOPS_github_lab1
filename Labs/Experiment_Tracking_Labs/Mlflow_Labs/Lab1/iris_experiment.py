import logging
import warnings

import mlflow
import mlflow.sklearn
import numpy as np
from mlflow.models import infer_signature
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


def eval_metrics(actual, pred):
    accuracy = accuracy_score(actual, pred)
    f1 = f1_score(actual, pred, average="weighted")
    precision = precision_score(actual, pred, average="weighted")
    recall = recall_score(actual, pred, average="weighted")
    return accuracy, f1, precision, recall


def run_experiment(model, model_name, params, X_train, X_test, y_train, y_test):
    with mlflow.start_run(run_name=model_name):
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        accuracy, f1, precision, recall = eval_metrics(y_test, predictions)

        print(f"\n{model_name}:")
        print(f"  Accuracy:  {accuracy:.4f}")
        print(f"  F1 Score:  {f1:.4f}")
        print(f"  Precision: {precision:.4f}")
        print(f"  Recall:    {recall:.4f}")

        # Log parameters
        for key, value in params.items():
            mlflow.log_param(key, value)

        # Log metrics
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("f1_score", f1)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)

        # Log model with signature
        signature = infer_signature(X_train, model.predict(X_train))
        mlflow.sklearn.log_model(
            model,
            artifact_path="model",
            signature=signature,
            registered_model_name=f"Iris_{model_name.replace(' ', '_')}",
        )

        mlflow.set_tag("dataset", "Iris")
        mlflow.set_tag("model_type", model_name)


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(42)

    # Load Iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Scale features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Set MLflow experiment name
    mlflow.set_experiment("Iris_Classification_Experiments")

    print("Running MLflow experiments on Iris dataset...")
    print("=" * 50)

    # --- Experiment 1: Logistic Regression ---
    lr_params = {"C": 1.0, "max_iter": 200, "solver": "lbfgs"}
    lr_model = LogisticRegression(**lr_params, random_state=42)
    run_experiment(
        lr_model, "Logistic Regression", lr_params, X_train, X_test, y_train, y_test
    )

    # --- Experiment 2: Random Forest ---
    rf_params = {"n_estimators": 100, "max_depth": 5, "min_samples_split": 2}
    rf_model = RandomForestClassifier(**rf_params, random_state=42)
    run_experiment(
        rf_model, "Random Forest", rf_params, X_train, X_test, y_train, y_test
    )

    # --- Experiment 3: SVM ---
    svm_params = {"C": 1.0, "kernel": "rbf", "gamma": "scale"}
    svm_model = SVC(**svm_params, probability=True)
    run_experiment(
        svm_model, "SVM", svm_params, X_train, X_test, y_train, y_test
    )

    print("\n" + "=" * 50)
    print("All experiments logged!")
    print("Run: mlflow ui")
    print("Then open: http://localhost:5000")
