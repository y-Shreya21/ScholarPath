import pickle
import numpy as np

MODEL_PATH = "model/fraud_model.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

def predict_fraud(features: dict):
    X = np.array([list(features.values())])
    
    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0][pred]

    return {
        "is_valid": bool(pred),
        "confidence": float(prob)
    }