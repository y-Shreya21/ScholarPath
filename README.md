# 🎓 ScholarPath — AI-Powered Document Verification System

An intelligent document verification platform for scholarship systems using **OCR + Machine Learning + Rule Engine + RAG (Retrieval-Augmented Generation)**.

---

## 🚀 Overview

ScholarPath automates the verification of student documents such as marksheets and income certificates by combining:

* 🧾 OCR for text extraction
* 🧠 ML model for fraud detection
* ⚖️ Rule-based validation
* 📚 RAG for explainable decisions

👉 The system not only predicts validity but also **explains *why*** a document is accepted or rejected.

---

## 🏗️ Architecture

```text
Upload Document
   ↓
OCR (Text Extraction)
   ↓
Document Type Detection
   ↓
Feature Extraction
   ↓
Rule Engine
   ↓
ML Model Prediction
   ↓
RAG (Rule Retrieval + Explanation)
   ↓
Final Decision
```

---

## ✨ Features

* 📄 Supports image-based documents (PNG, JPG)
* 🔍 OCR using Tesseract
* 🧠 ML-based fraud detection (Random Forest)
* ⚖️ Rule-based validation (income thresholds, document completeness)
* 📚 RAG-based explanation system
* ⚡ FastAPI backend with interactive Swagger UI
* 🧩 Modular and extensible architecture

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **ML:** scikit-learn (Random Forest)
* **OCR:** pytesseract + OpenCV
* **RAG:** JSON-based rule retrieval (extendable to FAISS)
* **Frontend:** React + Vite (in progress)

---

## 📂 Project Structure

```
backend/
├── data/
│   ├── raw/                # Training images
│   ├── labels.json        # ML labels
│   └── rules.json         # RAG rules
│
├── services/
│   ├── ocr.py             # OCR extraction
│   ├── feature.py         # Feature engineering
│   ├── model.py           # ML model
│   ├── rules.py           # Rule engine
│   ├── rag.py             # RAG logic
│   └── llm.py             # (future use)
│
├── main.py                # FastAPI app
├── train.py               # Model training script
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/scholarpath.git
cd scholarpath/backend

python -m venv venv
source venv/bin/activate   # mac/linux
venv\Scripts\activate      # windows

pip install -r requirement.txt
```

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

Open:

👉 http://127.0.0.1:8000/docs

---

## 🧪 API Usage

### POST `/verify`

Upload an image file.

### Example Response:

```json
{
  "doc_type": "marksheet",
  "features": {
    "income": 42,
    "text_length": 322
  },
  "rule_result": {
    "status": "Accepted",
    "reason": "No rule violations"
  },
  "ml_prediction": {
    "is_valid": true,
    "confidence": 0.75
  },
  "explanation": "Accepted. Rule satisfied: Document must contain valid marks and student details"
}
```

---

## 🧠 Key Concepts

### 🔹 Rule Engine

Applies deterministic checks:

* Income thresholds
* Document completeness

### 🔹 Machine Learning

Learns patterns from labeled data:

* Fraud detection
* Anomaly scoring

### 🔹 RAG (Retrieval-Augmented Generation)

* Retrieves relevant rules from knowledge base
* Generates human-readable explanations

---

## 📊 Model Training

```bash
python train.py
```

* Uses features extracted from documents
* Trains Random Forest classifier
* Saves model as `fraud_model.pkl`

---

## ⚠️ Limitations

* Small dataset → limited model accuracy
* OCR noise affects feature extraction
* Basic RAG (keyword-based, not semantic yet)

---

## 🚀 Future Improvements

* 🔥 FAISS-based semantic RAG
* 📄 PDF support
* 🎯 Better feature extraction (name, income parsing)
* 🌐 Full frontend dashboard
* ☁️ Deployment (AWS / Render / Docker)

---

## 💡 Why This Project Stands Out

* Combines **ML + Rules + RAG** (real-world architecture)
* Focus on **explainability**, not just prediction
* Modular design for multiple document types
* Solves a real problem in scholarship verification

---

## 👩‍💻 Author

Shreya Yadav
Machine Learning Engineer

---

## ⭐ If you like this project

Give it a star ⭐ and share feedback!
