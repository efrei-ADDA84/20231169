# Image de base Python
FROM python:3.8

# Définit le répertoire de travail Et le fichier contenant
# les dépendances à installer à l'intérieur du conteneur 
WORKDIR /app
COPY requirements.txt .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie tout le contenu du répertoire local vers le conteneur Docker
COPY . .
EXPOSE 80

# Exécution de l'application
CMD ["python", "api_openweather_v2.py"]
