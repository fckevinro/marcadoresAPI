from fastapi import FastAPI
import requests 
app = FastAPI()


def get_data():
    url = "https://api.sofascore.com/api/v1/sport/football/events/live"  # Reemplaza esto con la URL real de tu API

# Definir el agente de usuario de Firefox
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"

    # Configurar el encabezado de la solicitud con el agente de usuario
    headers = {"User-Agent": user_agent}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Parsear el JSON y trabajar con los datos según sea necesario
        data = response.json()


        # Ahora puedes acceder a los datos en el JSON
        # Por ejemplo, para acceder a la lista de eventos:
        eventos = data["events"]

        print(data['events'][0].keys())

        
        
        # Para acceder a la información de un evento específico, por ejemplo, el primer evento:
        primer_evento = eventos[0]
        
        # Puedes acceder a diferentes campos dentro del evento, por ejemplo, el nombre del torneo:
        # Y así sucesivamente para otros campos de datos que necesites.

        # Puedes realizar operaciones adicionales con los datos según tus necesidades.
        return eventos
    else:
        print("Error al realizar la solicitud a la API. Código de estado:", response.status_code)



@app.get("/partidos")
def obtener_saludo():
    eventos = get_data()
    return eventos


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
