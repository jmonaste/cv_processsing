import logging
import os
from logging.handlers import RotatingFileHandler

# Crear una función para configurar el logger
def setup_logger(name, log_file='logs/app.log', level=logging.INFO):
    """
    Configura un logger con un archivo rotativo.

    :param name: Nombre del logger.
    :param log_file: Ruta del archivo de log.
    :param level: Nivel de log (DEBUG, INFO, WARNING, ERROR, CRITICAL).
    :return: Logger configurado.
    """
    # Crear la carpeta de logs si no existe
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Configurar formato del logger
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Crear manejador de archivo con rotación
    handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
    handler.setFormatter(formatter)

    # Configurar el logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
