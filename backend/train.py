import json
import os
from services.feature import extract_features
from sklearn.ensemble import RandomForestClassifier
import pickle

DATA_DIR = "data/raw/"
LABELS_PATH = "data/labels.json"

with open(LABELS_PATH) as f:
    labels = json.load(f)

X, y = [], []

for file, info in labels.items():
    path = os.path.join(DATA_DIR, file)
    if not os.path.exists(path):
        print(f"❌ Missing file: {path}")
        continue

    
    features = extract_features(path)
    X.append(list(features.values()))
    y.append(1 if info["is_valid"] else 0)

model = RandomForestClassifier()
model.fit(X, y)

with open("model/fraud_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")