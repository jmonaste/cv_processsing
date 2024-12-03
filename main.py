from openai import OpenAI
from dotenv import load_dotenv
from utils.pdf_processor import PDFProcessor
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la clave API
pdf_path = os.getenv("PDF_PATH")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  # This is the default and can be omitted
)

def obtener_respuesta_llm(pdf_path):
    # Definir el prompt y los mensajes para ChatGPT
    messages = [
        {
            "role": "system",
            "content": [{"type": "text", "text": "Eres un asistente que etiqueta temas basándose en palabras clave proporcionadas. Proporciona un nombre descriptivo y conciso para cada conjunto de palabras clave."}]
            
        },
        {
            "role": "user",
            "content": [{"type": "text", "text": "Estas son las palabras clave de un tema: aeroespacial, tecnologia, vuelos, aerodinamica. Proporciona un nombre descriptivo para este tema en español."}]
        }
    ]
    
    try:
        chat_completion  = client.chat.completions.create(
            model="gpt-4",  # Asegúrate de usar el modelo correcto
            messages=messages,
            max_tokens=20,       # Ajusta según la longitud esperada del label
            temperature=0.3,     # Controla la creatividad de la respuesta
            n=1,                 # Número de respuestas a generar
            stop=None
        )
        # Obtener el contenido del mensaje de la respuesta
        return chat_completion
    except Exception as e:
        print(f"Error al etiquetar el tema: {e}")
        return "Tema Desconocido"

def print_llm_response(chat_completion):
    # Accediendo y mostrando parámetros de la respuesta
    print("Chat Completion Details:")
    print(f"ID: {chat_completion.id}")
    print(f"Model: {chat_completion.model}")
    print(f"Object: {chat_completion.object}")
    print(f"Created at (timestamp): {chat_completion.created}")
    print(f"Choices:")

    for idx, choice in enumerate(chat_completion.choices):
        print(f"  Choice {idx + 1}:")
        print(f"    Index: {choice.index}")
        print(f"    Finish Reason: {choice.finish_reason}")
        print(f"    Message Content: {choice.message.content}")
        print(f"    Role: {choice.message.role}")

    print("Usage Details:")
    print(f"  Prompt Tokens: {chat_completion.usage.prompt_tokens}")
    print(f"  Completion Tokens: {chat_completion.usage.completion_tokens}")
    print(f"  Total Tokens: {chat_completion.usage.total_tokens}")



#chat_completion = obtener_respuesta_llm(pdf_path)

# Crear una instancia de PDFProcessor
processor = PDFProcessor(pdf_path)

# Extraer texto
text = processor.extract_text()

# Mostrar el texto extraído o guardarlo
if text:
    print("Texto extraído del PDF:")
    print(text)
else:
    print("No se pudo extraer texto del PDF.")

