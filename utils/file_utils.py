import os

def is_file_exists(file_path):
    """
    Verifica si un archivo existe.
    """
    return os.path.exists(file_path) and os.path.isfile(file_path)
