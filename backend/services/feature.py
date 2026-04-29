import re
import cv2
from rapidfuzz import fuzz
from services.ocr import extract_text

INCOME_THRESHOLD = 250000

def extract_income(text):
    matches = re.findall(r'\d{1,3}(?:,\d{3})*', text)
    if matches:
        return int(matches[0].replace(",", ""))
    return 0

def blur_score(image_path):
    img = cv2.imread(image_path, 0)
    
    if img is None:
        return 0
    
    return cv2.Laplacian(img, cv2.CV_64F).var()
def extract_features(image_path, reference_name="Ravi Kumar"):
    text = extract_text(image_path)

    income = extract_income(text)
    name_similarity = fuzz.partial_ratio(reference_name, text)

    features = {
        "income": income,
        "income_exceeds": int(income > INCOME_THRESHOLD),
        "name_similarity": name_similarity,
        "text_length": len(text),
        "blur": blur_score(image_path)
    }

    return features
def detect_doc_type(text):
    text = text.lower()
    
    if "marksheet" in text or "examination" in text:
        return "marksheet"
    elif "income certificate" in text:
        return "income"
    
    return "unknown"