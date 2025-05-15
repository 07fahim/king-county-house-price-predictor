import numpy as np
import joblib
import os
from app.schemas.house import HouseFeatures
from typing import Any

# Paths
MODEL_PATH = os.path.join('data', 'model.pkl')
SCALER_PATH = os.path.join('data', 'scaler.pkl')
USE_SCALER_PATH = os.path.join('data', 'use_scaler.txt')

# Model instances (lazy loading)
_model = None
_scaler = None
_use_scaler = os.path.exists(USE_SCALER_PATH)

def get_model():
    """Lazy loading of the ML model"""
    global _model, _scaler
    if _model is None:
        try:
            _model = joblib.load(MODEL_PATH)
            if _use_scaler:
                _scaler = joblib.load(SCALER_PATH)
        except Exception as e:
            raise RuntimeError(f"Failed to load model: {str(e)}")
    return _model

def predict_price(model: Any, features: HouseFeatures) -> float:
    """Predict house price using the loaded model"""
    # Extract features in the correct order
    feature_array = np.array([
        features.sqft_living,
        features.grade,
        features.bathrooms,
        features.bedrooms,
        features.waterfront,
        features.view,
        features.sqft_basement,
        features.yr_built,
        features.lat,
        features.long
    ]).reshape(1, -1)
    
    # Apply scaling if needed
    if _use_scaler:
        feature_array = _scaler.transform(feature_array)
    
    # Make prediction
    prediction = model.predict(feature_array)
    
    # Return the prediction as a float
    return float(prediction[0])