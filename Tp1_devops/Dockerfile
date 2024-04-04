# Image de base Python
FROM python:3.9-slim

# Copie le code du wrapper dans l'image
COPY . /app
WORKDIR /app

# Installe les dépendances
RUN pip install requests

# Exécution de l'application
CMD ["python", "openweatherWrapper.py"]
