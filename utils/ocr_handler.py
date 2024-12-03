from pdf2image import convert_from_path
import pytesseract
import os
from utils.logger import setup_logger

# Configurar el logger para este módulo
logger = setup_logger(__name__)

def apply_ocr(pdf_path):
    """
    Convierte un PDF a imágenes y aplica OCR para extraer texto.
    
    :param pdf_path: Ruta al archivo PDF que se procesará.
    :return: Texto extraído del PDF.
    """
    try:
        if not os.path.exists(pdf_path):
            logger.error(f"El archivo '{pdf_path}' no existe.")
            raise FileNotFoundError(f"El archivo '{pdf_path}' no existe.")

        logger.info(f"Iniciando OCR para el archivo '{pdf_path}'.")
        text = ""
        
        # Convertir PDF a imágenes
        images = convert_from_path(pdf_path)
        logger.info(f"Se generaron {len(images)} imágenes a partir del PDF '{pdf_path}'.")

        # Aplicar OCR a cada imagen
        for i, img in enumerate(images, start=1):
            logger.debug(f"Aplicando OCR a la página {i} del PDF '{pdf_path}'.")
            text += pytesseract.image_to_string(img)
        
        logger.info(f"OCR completado para el archivo '{pdf_path}'.")
        return text
    except Exception as e:
        logger.error(f"Error aplicando OCR al PDF '{pdf_path}': {e}", exc_info=True)
        return ""
