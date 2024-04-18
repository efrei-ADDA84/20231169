from flask import Flask, request, jsonify, render_template
import os
import requests

app_v2 = Flask(__name__)

# Redéfinition de la fonction get_weather(lat, long)
def get_weather(latitude, longitude):
    """
    Cette fonction nous permet de renvoyer la météo d'un lieu donné à partir 
    de la latitude et la longitude données en paramètre.
    La clé API est récupérée des variables d'environnement du système
    """
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    base_url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
    
    response = requests.get(base_url)     
    if response.status_code == 200:
        data = response.json()
        weather_data = data.get("weather", [])[0]            #data["weather"][0]
        place_name = data.get("name")                        #data["name"]
        return weather_data, place_name
    else:
        print("Erreur lors de la requête : ", response.status_code)
        return None


# Définition d'une route qui accepte les méthodes GET
@app_v2.route('/')
def api_weather():
    
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')
    if latitude and longitude:
        weather, place_name = get_weather(latitude, longitude)
        return jsonify({"weather": weather, "place": place_name}), 200
        #return render_template('index.html', weather=weather, place_name=place_name)
    else:
        return jsonify({'error': 'Unable to fetch weather data'}), 500

if __name__ == "__main__":
    # Si l'on souhaite que l'application écoute le port 8081 (5000 par défaut)
    app_v2.run(debug=True, host='0.0.0.0', port=80)    # 80:81   

