import os
import requests

def get_weather_by_coordinates():       

    # On fait appel aux variables d'environnement créées contenant la clé api, la latitude et la longitude
    latitude = os.environ.get('LAT')
    longitude = os.environ.get('LONG')
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    
    base_url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
    
    response = requests.get(base_url)     
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Erreur lors de la requête : ", response.status_code)
        return None

if __name__ == "__main__":

    weather_data = get_weather_by_coordinates() 

    if weather_data:
        # Si on veut retourner tous les champs concernant les conditions météorologiques
        # print("Météo actuelle : ", weather_data)

        # Si on veut retourner uniquement le champs "weather" avec moins d'info
        weather_info = weather_data["weather"][0]
        place_name = weather_data["name"]
        print(f"Météo actuelle : {weather_info}")

        # Pour avoir le nom du lieu correspondant aux coordonnées données
        print(f"Lieu : {place_name}")       

