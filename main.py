from openai import OpenAI
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la clave API
imagen_path = os.getenv("IMAGE_PATH")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  # This is the default and can be omitted
)

#openai.error.InvalidRequestError: 'chat response' is not one of ['fine-tune', 'assistants', 'batch', 'user_data', 'responses', 'vision', 'evals'] - 'purpose'

def obtener_json_ticket(imagen_path):
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


chat_completion = obtener_json_ticket(imagen_path)

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

