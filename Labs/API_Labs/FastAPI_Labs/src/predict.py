import joblib
import os

def load_model():
    """Load the trained model from file."""
    model_path = os.path.join(os.path.dirname(__file__), "..", "model", "iris_model.pkl")
    model = joblib.load(model_path)
    return model

def predict_data(X):
    """Predict the class labels for the input data."""
    model = load_model()
    y_pred = model.predict(X)
    return y_pred

def predict_with_confidence(X):
    """Predict class labels along with confidence score."""
    model = load_model()
    y_pred = model.predict(X)
    probabilities = model.predict_proba(X)
    confidence = max(probabilities[0])
    return y_pred, confidence