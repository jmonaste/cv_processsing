import os
from utils.logger import setup_logger

# Configurar el logger para este módulo
logger = setup_logger(__name__)

def is_file_exists(file_path):
    """
    Verifica si un archivo existe.

    :param file_path: Ruta al archivo que se desea verificar.
    :return: True si el archivo existe y es un archivo regular, False en caso contrario.
    """
    try:
        if os.path.exists(file_path):
            if os.path.isfile(file_path):
                logger.info(f"El archivo '{file_path}' existe y es válido.")
                return True
            else:
                logger.warning(f"La ruta '{file_path}' existe, pero no es un archivo regular.")
                return False
        else:
            logger.warning(f"El archivo '{file_path}' no existe.")
            return False
    except Exception as e:
        logger.error(f"Error al verificar si el archivo '{file_path}' existe: {e}", exc_info=True)
        return False
