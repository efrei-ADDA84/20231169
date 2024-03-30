import os
import requests

class OpenWeatherWrapper:
    def __init__(self):

        # on fait appel a la variable d'environnement créée contenant la clé api
        self.api_key = os.environ.get('OPENWEATHER_API_KEY')
        self.base_url = 'https://api.openweathermap.org/data/2.5/weather'

    def get_weather_by_coordinates(self, latitude, longitude):
        params = {
            'lat': latitude,
            'lon': longitude,
            'appid': self.api_key,
            'units': 'metric'  # Unité de mesure (metric pour Celsius)
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Erreur lors de la requête : ", response.status_code)
            return None

if __name__ == "__main__":
    wrapper = OpenWeatherWrapper()
    latitude = float(input("Entrez la latitude : "))
    longitude = float(input("Entrez la longitude : "))
    weather_data = wrapper.get_weather_by_coordinates(latitude, longitude)
    if weather_data:

        # si on veut retourner tous les champs concernant les conditions météorologiques
        #print("Météo actuelle : ", weather_data)

        # si on veut retourner uniquement le champs "weather" avec moins d'info
        weather_info = weather_data["weather"][0]
        place_name = weather_data["name"]
        print(f"Météo actuelle : {weather_info}")
        # pour avoir le nom du lieu correspondant aux coordonnées données
        print(f"Lieu : {place_name}")       

