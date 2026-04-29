from fastapi import FastAPI, UploadFile, File
import shutil
import os

from services.ocr import extract_text
from services.feature import extract_features, detect_doc_type
from services.model import predict_fraud
from services.rules import rule_check
from services.rag import retrieve_rule, generate_explanation

app = FastAPI()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "temp")

os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/verify")
async def verify_document(file: UploadFile = File(...)):
    try:
        # ✅ File type check
        if not file.filename.lower().endswith((".png", ".jpg", ".jpeg")):
            return {"error": "Only image files supported (png, jpg, jpeg)"}

        file_path = f"{UPLOAD_DIR}/{file.filename}"

        # Save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 🔥 STEP 1 — OCR (FIRST)
        text = extract_text(file_path)

        # 🔥 STEP 2 — Detect document type
        doc_type = detect_doc_type(text)

        # 🔥 STEP 3 — Feature extraction (single call)
        features = extract_features(file_path)

        # 🔥 STEP 4 — Rule engine
        rule_result = rule_check(features, doc_type)
        rule_text = retrieve_rule(doc_type)
        explanation = generate_explanation(rule_text, features, rule_result)

        # 🔥 STEP 5 — ML prediction
        ml_result = predict_fraud(features)

        return {
            "doc_type": doc_type,
            "text_preview": text[:200],
            "features": features,
            "rule_result": rule_result,
            "ml_prediction": ml_result,
             "explanation": explanation
        }

    except Exception as e:
        return {"error": str(e)}