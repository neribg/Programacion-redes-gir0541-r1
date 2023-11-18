'''
Descripcion: Consumiendo API con Python 
Autor: Felipe Neri Francisco Bueno González 
Fecha: 17 de noviembre del 2023
'''

import requests

def get_weather(latitude, longitude):
    url = "https://api.tomorrow.io/v4/weather/forecast?location={latitude},{longitude}&apikey={api_key}".format(
        latitude=latitude, longitude=longitude, api_key="MdB7Rya43kpk2N1Wu24XXSdueAFvNjqO"
    )
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos_json = respuesta.json()
        estado_json = datos_json["forecast"]["forecastday"][0]["weather"][0]["description"]
        return estado_json
    else:
        print("Hubo un error con la llamada a la API.")
        return None


while True:
    try:
        latitude = float(input("Introduce la latitud: "))
        longitude = float(input("Introduce la longitud: "))

        if not isinstance(latitude, float) or not isinstance(longitude, float):
            print("La longitud y latitud deben ser números.")
            continue

        estado = get_weather(latitude, longitude)

        if estado is None:
            print("No se pudo obtener el clima.")
        else:
            print(f"El clima en {latitude}, {longitude} es {estado}")
    except ValueError:
        print("La longitud y latitud deben ser números.")
        