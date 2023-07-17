import requests
import json
from datetime import datetime
import random

# URL de la API
url = "http://localhost:8000/anime_notes/"

# Obtener la fecha actual
fecha_actual = datetime.now().strftime("%Y-%m-%d")

# Realizar la solicitud POST por cada registro
for _ in range(5):
    # Crear el registro
    registro = {
        "note_name": "Nombre de la nota",
        "text_note": "Contenido de la nota",
        "date_note": fecha_actual
    }

    # Realizar la solicitud POST para el registro actual
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps(registro)
    response = requests.post(url, headers=headers, data=data)

    # Verificar el resultado
    if response.status_code == 201:
        print("Registro enviado exitosamente")
    else:
        print("Error en el envío del registro:", response.status_code)
        print(response.text)
