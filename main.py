import os
from dotenv import load_dotenv
from openai import OpenAI
from utils.pdf_processor import PDFProcessor
from utils.logger import setup_logger

# Configurar el logger
logger = setup_logger(__name__)

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la clave API
pdf_path = os.getenv("PDF_PATH")
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    logger.error("No se encontró la clave API en las variables de entorno.")
    raise ValueError("API key no encontrada.")

if not pdf_path:
    logger.error("No se especificó la ruta del PDF en las variables de entorno.")
    raise ValueError("Ruta del PDF no especificada.")

# Crear cliente de OpenAI
client = OpenAI(api_key=api_key)


def obtener_respuesta_llm(client, pdf_path):
    """
    Envía un prompt al modelo de OpenAI para obtener una etiqueta temática basada en palabras clave.

    :param client: Cliente OpenAI configurado.
    :param pdf_path: Ruta del archivo PDF procesado.
    :return: Objeto con la respuesta del modelo.
    """
    messages = [
        {
            "role": "system",
            "content": "Eres un asistente que etiqueta temas basándose en palabras clave proporcionadas. Proporciona un nombre descriptivo y conciso para cada conjunto de palabras clave."
        },
        {
            "role": "user",
            "content": "Estas son las palabras clave de un tema: aeroespacial, tecnologia, vuelos, aerodinamica. Proporciona un nombre descriptivo para este tema en español."
        }
    ]
    
    try:
        logger.info("Enviando solicitud a OpenAI para etiquetar tema...")
        chat_completion = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            max_tokens=20,
            temperature=0.3,
            n=1,
            stop=None
        )
        logger.info("Respuesta recibida de OpenAI.")
        return chat_completion
    except Exception as e:
        logger.error("Error al etiquetar el tema con OpenAI.", exc_info=True)
        return None


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
    chat_completion = obtener_respuesta_llm(client, pdf_path)

    # Imprimir detalles de la respuesta
    print_llm_response(chat_completion)

    logger.info("Proceso completado.")


if __name__ == "__main__":
    main()
