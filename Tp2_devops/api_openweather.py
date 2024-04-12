from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

# Définition d'une route /weather ('http://<adresse_ip>:<port>/weatger') qui accepte les méthodes GET
@app.route('/weather', methods=['GET'])
def get_weather():
    """
    Cette fonction nous permet de récupérer les valeurs de latitude, longitude 
    ainsi que la clé API à partir des variables d'environnement du système
    """
    latitude = os.environ.get('LAT')
    longitude = os.environ.get('LONG')
    api_key = os.environ.get('OPENWEATHER_API_KEY')

    base_url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'

    # Récupère les données météorologiques depuis l'API openweather
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        weather_info = data.get("weather", [])[0]
        place_name = data.get("name")
        return jsonify({"weather": weather_info, "place": place_name}), 200
    else:
        return jsonify({'error': 'Unable to fetch weather data'}), 500

if __name__ == "__main__":
    app.run(debug=True)
