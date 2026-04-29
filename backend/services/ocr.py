import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract" 

def extract_text(image_path):
    img = cv2.imread(image_path)

    if img is None:
        return ""   # prevent crash

    text = pytesseract.image_to_string(img)
    return text