import PyPDF2
from utils.ocr_handler import apply_ocr
from utils.file_utils import is_file_exists

class PDFProcessor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.text = None

    def is_native_pdf(self):
        """
        Verifica si el PDF es nativo (con texto seleccionable).
        """
        try:
            with open(self.pdf_path, 'rb') as f:
                pdf_reader = PyPDF2.PdfReader(f)
                for page in pdf_reader.pages:
                    if page.extract_text().strip():
                        return True
            return False
        except Exception as e:
            print(f"Error verificando si el PDF es nativo: {e}")
            return False

    def extract_text(self):
        """
        Extrae texto del PDF. Si no es nativo, aplica OCR.
        """
        if not is_file_exists(self.pdf_path):
            raise FileNotFoundError(f"El archivo {self.pdf_path} no existe.")
        
        if self.is_native_pdf():
            print("El PDF es nativo. Extrayendo texto...")
            self.text = self._extract_text_native()
        else:
            print("El PDF no es nativo. Aplicando OCR...")
            self.text = apply_ocr(self.pdf_path)
        return self.text

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
            return text
        except Exception as e:
            print(f"Error extrayendo texto del PDF nativo: {e}")
            return ""
