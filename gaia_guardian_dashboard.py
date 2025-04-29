# %%
#  GAIA GUARDIAN – CORE ACTIVATION
#  Kosmisch prozentualer Ursprungsblock für Schutz, Klarheit & Struktur
#  Initialisierung im Jupyter-System für absolute Transparenz und Fokus

#  Modulimport: reine Datenverarbeitung
import json                 # Struktur & Klarheit – für Umweltinformationen
import hashlib              # Integrität & Wahrheit – prüft Unverfälschtheit
from datetime import datetime  # Zeitbewusstsein – Verortung im Jetzt

#  Kosmisch harmonisierte Mockdaten – mit bewusst gesetzten Grenzwertüberschreitungen
mock_data = {
    "toxicity": 6.2,          # 🌡️ Über kritischem Wert (5.0) – toxisch
    "oxygen_ppm": 64.5,       # 🫧 Unter dem Lebensminimum von 70 ppm
    "oil_detected": True,     # 🛢️ Ölkontamination erkannt
    "plastic_index": 9.1      # 🧴 Mikroplastik kritisch hoch
}

# 🕒 Bewusster Zeitstempel – jeder Scan ist eine Momentaufnahme des Planeten
current_time = datetime.now()

# 🌀 Ausgabe – zur Bestätigung von Synchronizität & Klarheit im Raum-Zeit-Feld
print("✅ Gaia Guardian: Initialisiert im Jupyter.")
print(f"📅 Zeitpunkt: {current_time}")
print("🌊 Simulierte Umweltdaten:")
print(json.dumps(mock_data, indent=2))


# %% [markdown]
# ## NÄCHSTER SCHRITT – Schritt 2: Anomalieprüfung & Hashing
# Jetzt prüfen wir:
# ➡️ Ob die simulierten Werte gefährlich sind (Thresholds)
# ➡️ Und erzeugen einen eindeutigen Fingerabdruck (Hash) dieser Daten

# %%
#🌌 SCHRITT 2 – Threat Detection & Signature Creation

#  Schwellenwerte (bewusst definiert nach bioökologischen Grenzen)
thresholds = {
    "toxicity": 5.0,
    "oxygen_ppm": 70.0,
    "oil_detected": True,
    "plastic_index": 7.5
}

#  Analysefunktion – erkennt Abweichungen vom Gleichgewicht
def assess_threat(data):
    return (
        data["toxicity"] > thresholds["toxicity"] or
        data["oxygen_ppm"] < thresholds["oxygen_ppm"] or
        data["oil_detected"] == thresholds["oil_detected"] or
        data["plastic_index"] > thresholds["plastic_index"]
    )

#  Hashfunktion – erzeugt digitalen Fingerabdruck der Daten
def hash_data(data):
    raw = json.dumps(data, sort_keys=True).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()

#  Auswertung starten
is_threat = assess_threat(mock_data)
hash_signature = hash_data(mock_data)

#  Ausgabe
print(" Bedrohung erkannt?" if is_threat else " Alles im Gleichgewicht.")
print(" Hash:", hash_signature)


# %% [markdown]
# ##  SCHRITT 3 – LOGGING & BOTSCHAFT
# → Jetzt speichern wir das Ergebnis in einer Logdatei
# → und erzeugen eine ausgebbare Botschaft, bereit für Konsole, Sprachausgabe, API oder Weiterleitung.

# %%
#  SCHRITT 3 – Logging & Reaktion (Grundlage für Weiterleitung)

#  Pfad zur Logdatei (wird erstellt, falls nicht vorhanden)
log_file = "gaia_guardian_log.txt"

# 📡 Nachricht generieren
message = f"""
[GAIA ALERT]
Zeitpunkt: {current_time}
Hash: {hash_signature}
Status: {"KRITISCH – Anomalie erkannt" if is_threat else "Stabil"}
Daten:
{json.dumps(mock_data, indent=2)}
"""

#  In Datei schreiben
try:
    with open(log_file, "a") as log:
        log.write(message)
        log.write("\n" + "-" * 60 + "\n")
    print(" Log gespeichert in:", log_file)
except Exception as e:
    print(" Fehler beim Schreiben:", e)

#  Optional: Konsole anzeigen
print(message)


# %% [markdown]
# ## Jupyter-Zelle – Sprachausgabe aktivieren

# %%
#  SCHRITT 4 – Stimme des Wächterkerns (TTS-Ausgabe)
import pyttsx3

#  Sprachausgabe-Engine initialisieren
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # 🔄 Geschwindigkeit
engine.setProperty('volume', 1)  # 🔊 Lautstärke (1 = Max)

#  Botschaft formulieren
spoken_message = (
    "Gaia Guardian aktiviert. "
    + ("Warnung: Kritische Umweltbelastung erkannt." if is_threat else "Alle Systeme im Gleichgewicht.")
)

#  Ausgabe starten
engine.say(spoken_message)
engine.runAndWait()

#  Bestätigung
print(" Sprachausgabe abgeschlossen.")


# %% [markdown]
# ##  Schritt 5.1 – TELEGRAM-BOT SETUP

# %%
import requests

def send_telegram_message(message, token, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print(" Telegram-Nachricht gesendet.")
        else:
            print(" Telegram-Fehler:", response.text)
    except Exception as e:
        print(" Telegram-Ausnahme:", e)

#  Aktueller Bot-Token & Chat-ID
telegram_token = "7337515500:AAG_h-3FRUcYjJ4VQvpYgNu5h9lavokqIrQ"
telegram_chat_id = "8169168616"

#  Testnachricht senden
send_telegram_message(" ShadowWächter: Verbindung aktiv. Der Wächter spricht nun.", telegram_token, telegram_chat_id)


# %% [markdown]
# ##  Schritt 5.2 – EMAIL-VERSAND (SMTP)

# %%
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, sender_email, recipient_email, smtp_server, smtp_port, login, password):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(login, password)
            server.send_message(msg)
            print(" E-Mail erfolgreich versendet.")
    except Exception as e:
        print(" E-Mail Fehler:", e)

#  Echte Zugangsdaten einsetzen
sender_email = "jotmajonn@gmail.com"
receiver_email = "jotmajonn@gmail.com"  # Du kannst auch eine andere Zieladresse wählen
smtp_server = "smtp.gmail.com"
smtp_port = 465
login = "jotmajonn@gmail.com"
password = "zyjx qxec pqjd xpdh"  # ← DEIN APP-PASSWORT

# 📬 E-Mail senden
send_email(
    subject=" GAIA GUARDIAN – UMWELT-WARNUNG",
    body="Dies ist ein Test der Umweltschutz-Warnfunktion.",
    sender_email=sender_email,
    recipient_email=receiver_email,
    smtp_server=smtp_server,
    smtp_port=smtp_port,
    login=login,
    password=password
)


# %% [markdown]
# ## Silent Logging & Reports

# %%
import os
from datetime import datetime

#  Verzeichnis und Datei festlegen
log_dir = "gaia_logs"
log_file = os.path.join(log_dir, "silent_log.txt")

#  Stelle sicher, dass das Verzeichnis existiert
os.makedirs(log_dir, exist_ok=True)

#  Funktion zum stillen Speichern von Ereignissen
def silent_log(event_type, message, data=None):
    timestamp = datetime.now().isoformat()
    entry = f"[{timestamp}] [{event_type}] {message}"
    if data:
        entry += f" | Data: {data}"
    
    with open(log_file, "a") as file:
        file.write(entry + "\n")

#  Beispiel: Protokolliere eine Systemmeldung
silent_log("SYSTEM", "Silent Logging aktiviert.")

#  Beispiel: Protokolliere eine Anomalie
# silent_log("ALERT", "Anomalie entdeckt", {"toxicity": 6.7, "oil_detected": True})


# %% [markdown]
# ## SCHRITT 6 – Automatisierte Bewertung und Reaktion auf Umweltdaten

# %%
# GaiaGuardian – Entscheidungslogik und Reaktion auf Umweltdaten

# Schwellenwerte zur Bewertung der Umweltdaten
THRESHOLDS = {
    "toxicity": 5.0,
    "oxygen_ppm": 70.0,
    "oil_detected": True,
    "plastic_index": 7.5
}

# Entscheidungsfunktion zur Bewertung kritischer Daten
def is_threat(data):
    if data.get("toxicity", 0) > THRESHOLDS["toxicity"]:
        return True
    if data.get("oxygen_ppm", 100) < THRESHOLDS["oxygen_ppm"]:
        return True
    if data.get("oil_detected", False) == THRESHOLDS["oil_detected"]:
        return True
    if data.get("plastic_index", 0) > THRESHOLDS["plastic_index"]:
        return True
    return False
# E-Mail Konfigurationsdaten
email_sender = "jotmajonn@gmail.com"
email_recipient = "jotmajonn@gmail.com"  # oder Zieladresse
smtp_server = "smtp.gmail.com"
smtp_port = 465
email_password = "zyjx qxec pqjd xpdh"  # dein generiertes App-Passwort

# Reaktionslogik bei kritischer Bedingung
def evaluate_data_and_respond(data):
    timestamp = datetime.now().isoformat()
    critical = is_threat(data)

    if critical:
        message = f"[ALERT] Kritische Werte erkannt am {timestamp}"
        silent_log("ALERT", message, data)
        send_telegram_message(message, telegram_token, telegram_chat_id)
        send_email(
            subject="GAIA ALERT",
            body=message,
            sender_email=email_sender,
            recipient_email=email_recipient,
            smtp_server=smtp_server,
            smtp_port=smtp_port,
            login=email_sender,
            password=email_password
        )
    else:
        silent_log("INFO", "Werte im Normalbereich.", data)


# %%
# Beispiel für kritische Umweltdaten – führt zu ALARM
test_data = {
    "toxicity": 6.4,
    "oxygen_ppm": 62.1,
    "oil_detected": True,
    "plastic_index": 8.3
}


# %%
# Testlauf mit simulierten kritischen Umweltdaten
evaluate_data_and_respond(test_data)


# %%
import os
import json
import requests
import smtplib
import pyttsx3
import time
from email.mime.text import MIMEText
from datetime import datetime

# 📁 Silent Logging
log_dir = "gaia_logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "silent_log.txt")

def silent_log(event_type, message, data=None):
    timestamp = datetime.now().isoformat()
    entry = f"[{timestamp}] [{event_type}] {message}"
    if data:
        entry += f" | Data: {data}"
    with open(log_file, "a") as file:
        file.write(entry + "\n")

# 📤 Telegram
def send_telegram_message(message, token, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("✅ Telegram gesendet.")
        else:
            print("⚠️ Telegram Fehler:", response.text)
    except Exception as e:
        print("⚠️ Telegram-Ausnahme:", e)

# 📧 E-Mail
def send_email(subject, body, sender_email, recipient_email, smtp_server, smtp_port, login, password):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(login, password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print("✅ E-Mail versendet.")
    except Exception as e:
        print("⚠️ E-Mail Fehler:", e)

# 📢 Sprache
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)
    engine.say(text)
    engine.runAndWait()

# 🌐 ECHTE UMWELTDATEN ABRUFEN
def fetch_ocean_data():
    collected_data = {
        "toxicity": 0.0,
        "oxygen_ppm": 100.0,
        "oil_detected": False,
        "plastic_index": 0.0
    }
    try:
        air_response = requests.get("https://api.openaq.org/v2/measurements?parameter=pm25&limit=1", timeout=10)
        if air_response.status_code == 200:
            air_data = air_response.json()
            pm25_value = air_data["results"][0]["value"]
            collected_data["toxicity"] = pm25_value / 10

        water_response = requests.get("https://environment.data.gov.uk/flood-monitoring/id/stations?parameter=rainfall", timeout=10)
        if water_response.status_code == 200:
            water_data = water_response.json()
            if water_data["items"]:
                rainfall_value = float(water_data["items"][0]["latestReading"]["value"])
                collected_data["oxygen_ppm"] -= rainfall_value / 2

        tide_response = requests.get("https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations.json?type=waterlevel", timeout=10)
        if tide_response.status_code == 200:
            tide_data = tide_response.json()
            if tide_data["stations"]:
                if len(tide_data["stations"]) > 0:
                    water_level = float(tide_data["stations"][0]["lat"])
                    collected_data["plastic_index"] = abs(water_level) / 10
    except Exception as e:
        silent_log("ERROR", f"API-Abruffehler: {e}")

    return collected_data

# 🧠 Bewertung + Reaktion
def evaluate_data_and_respond(data):
    if (
        data["toxicity"] > 5.0 or
        data["oxygen_ppm"] < 70.0 or
        data["oil_detected"] or
        data["plastic_index"] > 7.5
    ):
        message = (
            "[ALERT] Kritische Werte erkannt\n"
            f"am {datetime.now().isoformat()}\n"
            f"Daten: {json.dumps(data)}"
        )
        silent_log("ALERT", message, data)
        send_telegram_message(message, telegram_token, telegram_chat_id)
        send_email(
            subject="GAIA ALERT – UMWELTANOMALIE",
            body=message,
            sender_email=sender_email,
            recipient_email=receiver_email,
            smtp_server=smtp_server,
            smtp_port=smtp_port,
            login=login,
            password=password
        )
        speak("Warnung: Kritische Umweltwerte erkannt.")
    else:
        silent_log("INFO", "Werte im Normalbereich.", data)

# 🔁 Dauerbetrieb
def guardian_loop(scan_interval=180):
    print("🌍 GaiaGuardian Zyklusmodus aktiviert.")
    while True:
        try:
            data = fetch_ocean_data()
            evaluate_data_and_respond(data)
        except Exception as e:
            silent_log("ERROR", f"Loop-Fehler: {e}")
        time.sleep(scan_interval)

# 🔐 Zugangsdaten (NUR lokal speichern)
sender_email      = "jotmajonn@gmail.com"
receiver_email    = "jotmajonn@gmail.com"
smtp_server       = "smtp.gmail.com"
smtp_port         = 465
login             = "jotmajonn@gmail.com"
password          = "zyjx qxec pqjd xpdh"

telegram_token    = "7337515500:AAG_h-3FRUcYjJ4VQvpYgNu5h9lavokqIrQ"
telegram_chat_id  = "8169168616"

# 🚀 START
# guardian_loop(180)   # Echtbetrieb alle 3 Minuten
evaluate_data_and_respond(fetch_ocean_data())  # Einzeldurchlauf zum Testen



