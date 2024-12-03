import os
from dotenv import load_dotenv
from openai import OpenAI
from utils.pdf_processor import PDFProcessor
from utils.logger import setup_logger
from textwrap import dedent
from models.curriculum import Curriculum





# Configurar el logger
logger = setup_logger(__name__)

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la clave API
pdf_path = "C:\\Projects\\Personal\\23_CV_Processing\\input\\Pablo Argandoña Medina.pdf"
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    logger.error("No se encontró la clave API en las variables de entorno.")
    raise ValueError("API key no encontrada.")

if not pdf_path:
    logger.error("No se especificó la ruta del PDF en las variables de entorno.")
    raise ValueError("Ruta del PDF no especificada.")

# Crear cliente de OpenAI
client = OpenAI(api_key=api_key)
MODEL = "gpt-4o-2024-08-06"


def get_curriculum(data: str):
    curriculum_prompt = '''
    You are a professional CV builder. Given a set of details, your task is to output a structured JSON object representing a resume. Ensure the JSON format matches the schema provided and is well-organized. The description field must be summarized and concise. The proficiency language field must be one of the following: Basic, Intermediate, Advanced, Native.
    '''
    completion = client.beta.chat.completions.parse(
        model=MODEL,
        messages=[
            {"role": "system", "content": dedent(curriculum_prompt)},
            {"role": "user", "content": data},
        ],
        response_format=Curriculum,
    )
    return completion.choices[0].message


def print_llm_response(chat_completion):
    """
    Imprime los detalles de la respuesta del modelo OpenAI.

    :param chat_completion: Objeto de respuesta del modelo.
    """
    if not chat_completion:
        logger.warning("No se recibió una respuesta válida del modelo.")
        return

    logger.info("Detalles de la respuesta del modelo:")
    print(f"ID: {chat_completion.id}")
    print(f"Model: {chat_completion.model}")
    print(f"Object: {chat_completion.object}")
    print(f"Created at (timestamp): {chat_completion.created}")

    for idx, choice in enumerate(chat_completion.choices):
        print(f"  Choice {idx + 1}:")
        print(f"    Index: {choice.index}")
        print(f"    Finish Reason: {choice.finish_reason}")
        print(f"    Message Content: {choice.message.content}")
        print(f"    Role: {choice.message.role}")

    usage = chat_completion.usage
    print("Usage Details:")
    print(f"  Prompt Tokens: {usage.prompt_tokens}")
    print(f"  Completion Tokens: {usage.completion_tokens}")
    print(f"  Total Tokens: {usage.total_tokens}")


def main():
    """
    Flujo principal de la aplicación.
    """
    # Extraer texto del PDF
    logger.info("Iniciando extracción de texto del PDF.")
    processor = PDFProcessor(pdf_path)

    text = processor.extract_text()

    if text:
        logger.info("Texto extraído correctamente del PDF.")
        logger.debug(f"Texto extraído: {text[:100]}...")  # Log con muestra del texto
    else:
        logger.error("No se pudo extraer texto del PDF.")
        return

    # Obtener respuesta del modelo LLM
    logger.info("Enviando texto extraído al modelo de OpenAI.")
    chat_completion = get_curriculum(text)
    print(chat_completion.content)

    # Imprimir detalles de la respuesta
    # print_llm_response(chat_completion)

    logger.info("Proceso completado.")


if __name__ == "__main__":
    main()
