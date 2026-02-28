from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import json
from data import load_data, split_data

def fit_model(X_train, y_train, X_test, y_test):
    """
    Train a Random Forest Classifier, evaluate accuracy, and save model + metadata.
    """
    rf_classifier = RandomForestClassifier(n_estimators=100, max_depth=4, random_state=42)
    rf_classifier.fit(X_train, y_train)

    # Calculate accuracy
    y_pred = rf_classifier.predict(X_test)
    accuracy = round(accuracy_score(y_test, y_pred) * 100, 2)
    print(f"Model Accuracy: {accuracy}%")

    # Save model
    joblib.dump(rf_classifier, "../model/iris_model.pkl")

    # Save model metadata
    metadata = {
        "model_type": "Random Forest Classifier",
        "n_estimators": 100,
        "max_depth": 4,
        "accuracy": accuracy,
        "features": ["sepal_length", "sepal_width", "petal_length", "petal_width"],
        "classes": ["Setosa", "Versicolor", "Virginica"]
    }
    with open("../model/model_metadata.json", "w") as f:
        json.dump(metadata, f, indent=4)

    print("Model and metadata saved successfully.")

if __name__ == "__main__":
    X, y = load_data()
    X_train, X_test, y_train, y_test = split_data(X, y)
    fit_model(X_train, y_train, X_test, y_test)