# Image de base Python
FROM python:3.9-slim

# Définit le répertoire de travail Et le fichier contenant
# les dépendances à installer à l'intérieur du conteneur 
WORKDIR /app
COPY requirements.txt .

# Installe les dépendances
RUN pip install -r requirements.txt

# Copie tout le contenu du répertoire local vers le conteneur Docker
COPY . .

# Exécution de l'application
CMD ["python", "api_openweather_v2.py"]
