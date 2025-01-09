import os
from loguru import logger

# Criação de diretório seguro
def create_directory(directory_path: str):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    logger.info(f"Directory ensured: {directory_path}")

# Configuração de logging
def setup_logging():
    logger.add("logs/app.log", rotation="10 MB", retention="7 days", level="INFO")
    logger.info("Logging initialized")

# Validação de arquivos de upload
def validate_image_file(file, allowed_extensions=("jpeg", "jpg", "png")):
    file_extension = file.filename.split(".")[-1].lower()
    if file_extension not in allowed_extensions:
        raise ValueError("Formato de arquivo não suportado")
    return True

# Conversão de listas para strings
def list_to_string(items: list):
    return ", ".join(items)

# Configuração de paths
def get_temp_file_path(filename: str):
    create_directory("temp")
    return os.path.join("temp", filename)
