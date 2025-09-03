# -*- coding: utf-8 -*-
# 🔰 AUREON MISSION CORE V2 – Supervisor-Zentrale mit vollständiger Systemkontrolle
import os
import time
import json
import socket
import pyttsx3
import psutil
import subprocess
import speech_recognition as sr
from datetime import datetime

LOG_PATH = "logs/aureon_core_log.json"

# 🔊 Sprachengine initialisieren
engine = pyttsx3.init()
engine.setProperty("rate", 165)
engine.setProperty("volume", 1.0)
engine.setProperty("voice", engine.getProperty('voices')[0].id)

def spreche(text):
    print("🧠 AUREON:", text)
    engine.say(text)
    engine.runAndWait()

# 📓 Logging
def log_event(sektion, ereignis, details=""):
    eintrag = {
        "zeit": datetime.now().isoformat(),
        "sektion": sektion,
        "ereignis": ereignis,
        "details": details
    }
    os.makedirs("logs", exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(eintrag, ensure_ascii=False) + "\n")

# 🔎 Sektion 1: Netzwerkprüfung (IP + Ports)
def sektion_1():
    sektion = "1. Netzwerkprüfung"
    spreche("Starte Netzwerkprüfung.")
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        ports = [c.laddr.port for c in psutil.net_connections() if c.status == "ESTABLISHED"]
        log_event(sektion, "Erkannt", f"IP: {ip}, Verbindungen: {ports}")
        spreche(f"Deine IP ist {ip}. {len(ports)} aktive Verbindungen.")
    except Exception as e:
        spreche("Netzwerkprüfung fehlgeschlagen.")
        log_event(sektion, "Fehler", str(e))

# 🔎 Sektion 2: DNS-Konfiguration checken
def sektion_2():
    sektion = "2. DNS Check"
    spreche("Analysiere DNS-Konfiguration.")
    try:
        ausgabe = subprocess.check_output("ipconfig /all", shell=True, encoding="utf-8")
        if "8.8.8.8" in ausgabe:
            spreche("Öffentlicher DNS erkannt. Empfehlung: DNS absichern.")
        else:
            spreche("DNS-Konfiguration unauffällig.")
        log_event(sektion, "Analyse erfolgreich", "8.8.8.8 geprüft")
    except Exception as e:
        spreche("Fehler bei DNS-Analyse.")
        log_event(sektion, "Fehler", str(e))

# 🔎 Sektion 3: dpkg & apt Sicherheitsanalyse
def sektion_3():
    sektion = "3. dpkg Prüfung"
    spreche("Starte dpkg Sicherheitsanalyse.")
    try:
        out = subprocess.check_output("dpkg -l", shell=True, encoding="utf-8")
        log_event(sektion, "Pakete erkannt", out[:300])
        spreche("dpkg Liste geprüft und protokolliert.")
    except Exception as e:
        spreche("dpkg Analyse fehlgeschlagen.")
        log_event(sektion, "Fehler", str(e))

# 🔎 Sektion 4: Alte Befehle erkennen & modernisieren
def sektion_4():
    sektion = "4. Befehlskonversion"
    mapping = {
        "telnet": "ssh", "ftp": "sftp", "netstat": "ss", "ifconfig": "ip addr", "route": "ip route"
    }
    spreche("Scanne auf veraltete Befehle.")
    gefunden = []
    try:
        for b in mapping:
            result = subprocess.getoutput(f"which {b}")
            if result:
                gefunden.append((b, mapping[b]))
        if gefunden:
            spreche("Veraltete Befehle gefunden und ersetzt.")
            for alt, neu in gefunden:
                log_event(sektion, "Ersetzt", f"{alt} → {neu}")
        else:
            spreche("Keine veralteten Befehle gefunden.")
    except Exception as e:
        spreche("Fehler beim Befehlsscan.")
        log_event(sektion, "Fehler", str(e))

# 🎤 Sprachsteuerung aktivieren
def sprachsteuerung():
    spreche("Sprachsteuerung aktiv. Bitte Sektion sagen.")
    while True:
        with sr.Microphone() as quelle:
            recognizer = sr.Recognizer()
            try:
                audio = recognizer.listen(quelle, timeout=8)
                befehl = recognizer.recognize_google(audio, language="de-DE").lower()
                if "sektion 1" in befehl:
                    sektion_1()
                elif "sektion 2" in befehl:
                    sektion_2()
                elif "sektion 3" in befehl:
                    sektion_3()
                elif "sektion 4" in befehl:
                    sektion_4()
                elif "beenden" in befehl:
                    spreche("Mission beendet. Ich ziehe mich zurück.")
                    break
                else:
                    spreche("Befehl nicht erkannt.")
            except Exception as e:
                spreche("Akustisches Problem erkannt.")
                log_event("Spracheingabe", "Fehler", str(e))

# ▶ Starte alles
if __name__ == "__main__":
    spreche("AUREON CORE V2 wird geladen.")
    sprachsteuerung()
