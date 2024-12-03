from pdf2image import convert_from_path
import pytesseract
import os

def apply_ocr(pdf_path):
    """
    Convierte un PDF a imágenes y aplica OCR para extraer texto.
    """
    try:
        text = ""
        images = convert_from_path(pdf_path)
        for img in images:
            text += pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Error aplicando OCR al PDF: {e}")
        return ""
