import PyPDF2
from utils.ocr_handler import apply_ocr
from utils.file_utils import is_file_exists
from utils.logger import setup_logger

class PDFProcessor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.text = None
        self.logger = setup_logger(__name__)  # Configurar el logger para la clase

    def is_native_pdf(self):
        """
        Verifica si el PDF es nativo (con texto seleccionable).
        """
        try:
            self.logger.info(f"Verificando si el PDF '{self.pdf_path}' es nativo.")
            with open(self.pdf_path, 'rb') as f:
                pdf_reader = PyPDF2.PdfReader(f)
                for page in pdf_reader.pages:
                    if page.extract_text().strip():
                        self.logger.info(f"El PDF '{self.pdf_path}' es nativo.")
                        return True
            self.logger.info(f"El PDF '{self.pdf_path}' no es nativo.")
            return False
        except Exception as e:
            self.logger.error(f"Error verificando si el PDF '{self.pdf_path}' es nativo: {e}", exc_info=True)
            return False

    def extract_text(self):
        """
        Extrae texto del PDF. Si no es nativo, aplica OCR.
        """
        if not is_file_exists(self.pdf_path):
            self.logger.error(f"El archivo '{self.pdf_path}' no existe.")
            raise FileNotFoundError(f"El archivo '{self.pdf_path}' no existe.")

        try:
            if self.is_native_pdf():
                self.logger.info(f"Extrayendo texto del PDF nativo '{self.pdf_path}'.")
                self.text = self._extract_text_native()
            else:
                self.logger.info(f"Aplicando OCR al PDF '{self.pdf_path}' no nativo.")
                self.text = apply_ocr(self.pdf_path)
            return self.text
        except Exception as e:
            self.logger.error(f"Error al extraer texto del PDF '{self.pdf_path}': {e}", exc_info=True)
            return ""

    def _extract_text_native(self):
        """
        Extrae texto de un PDF nativo.
        """
        try:
            text = ""
            with open(self.pdf_path, 'rb') as f:
                pdf_reader = PyPDF2.PdfReader(f)
                for page in pdf_reader.pages:
                    text += page.extract_text()
            self.logger.debug(f"Texto extraído del PDF '{self.pdf_path}' (primeros 100 caracteres): {text[:100]}...")
            return text
        except Exception as e:
            self.logger.error(f"Error extrayendo texto del PDF nativo '{self.pdf_path}': {e}", exc_info=True)
            return ""
