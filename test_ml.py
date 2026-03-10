import pytest
# TODO: add necessary import
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model, compute_model_metrics, inference


@pytest.fixture
def sample_data():
    """Create small sample training data for testing."""
    np.random.seed(42)
    X = np.random.rand(100, 5)
    y = np.random.randint(0, 2, 100)
    return X, y

# TODO: implement the first test. Change the function name and input as needed
def test_train_model_returns_random_forest(sample_data):
    """Test that train_model returns a RandomForestClassifier instance."""
    X, y = sample_data
    model = train_model(X, y)
    assert isinstance(model, RandomForestClassifier)


# TODO: implement the second test. Change the function name and input as needed
def test_inference_returns_correct_shape(sample_data):
    """Test that inference returns predictions with the same length as input."""
    X, y = sample_data
    model = train_model(X, y)
    preds = inference(model, X)
    assert preds.shape[0] == X.shape[0]


# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics_perfect_predictions():
    """Test that perfect predictions return precision, recall, and F1 of 1.0."""
    y = np.array([0, 1, 0, 1, 1])
    preds = np.array([0, 1, 0, 1, 1])
    precision, recall, fbeta = compute_model_metrics(y, preds)
    assert precision == 1.0
    assert recall == 1.0
    assert fbeta == 1.0
