# -*- coding: utf-8 -*-
import os
import requests
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)


# API-Key aus Umgebungsvariable holen
api_key = os.getenv("OPENAI_API_KEY")


# Ziel-URL
url = "https://api.openai.com/v1/chat/completions"

# Anfrage-Daten
payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Ich will sprechen."}],
    "temperature": 0.7
}

# Header mit API-Key
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# POST-Anfrage senden
response = requests.post(url, headers=headers, json=payload)

# Ausgabe
print("Antwort der API:")
print(response.json())
print("DEBUG-KEY:", os.getenv("OPENAI_API_KEY"))
