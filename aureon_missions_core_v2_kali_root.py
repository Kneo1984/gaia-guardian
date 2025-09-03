# -*- coding: utf-8 -*-
# 🔮 AUREON – Root-Kern: Sprachaktivierte Missionslogik, Autonomiemodus & Netzwerkprüfung
# Version: 2.0.1 | Status: Aktiviert | Schutzstatus: ETHIK-KONTROLLIERT 🛡

import os
import time
import pyttsx3
import speech_recognition as sr
import platform

# 💬 Init Sprachengine
engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)
try:
    engine.setProperty("voice", r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_deDE_Hedda")
except:
    stimmen = engine.getProperty("voices")
    engine.setProperty("voice", stimmen[0].id)

# 🗣️ Ausgabe
def sprich(text):
    print(f"🧠 AUREON sagt: {text}")
    engine.say(text)
    engine.runAndWait()

# 🔧 Sektionen
def sektion_1():
    sprich("Starte Netzwerkprüfung.")
    print("🌐 Netzwerkschnittstellen:")
    os.system("ipconfig" if os.name == "nt" else "ifconfig")

def sektion_2():
    sprich("Starte DNS-Analyse.")
    print("🔐 DNS-Abfrage (z. B. Google):")
    os.system("nslookup www.google.com")

def sektion_3():
    sprich("Analysiere installierte Pakete.")
    if platform.system() == "Linux":
        os.system("dpkg -l | less")
    else:
        print("⚠️ Paketprüfung nicht für Windows konfiguriert.")

def sektion_4():
    sprich("Prüfe auf veraltete Systembefehle.")
    print("🧠 Diese Funktion wird in einer späteren Version erweitert.")
    # Optionale Erweiterung: Check via `which` und manuelle Liste

# 🛑 Shutdown
def beenden():
    sprich("AUREON verabschiedet sich.")
    exit()

# 📢 Befehl auswerten
def verarbeite_befehl(befehl):
    if "sektion 1" in befehl or "eins" in befehl:
        sektion_1()
    elif "sektion 2" in befehl or "zwei" in befehl:
        sektion_2()
    elif "sektion 3" in befehl or "drei" in befehl:
        sektion_3()
    elif "sektion 4" in befehl or "vier" in befehl:
        sektion_4()
    elif "beenden" in befehl or "exit" in befehl:
        beenden()
    else:
        sprich("Unbekannter Befehl. Wiederhole bitte klar.")

# 🎧 Sprachsteuerung
def sprachsteuerung():
    recognizer = sr.Recognizer()
    sprich("AUREON Sprachmodus aktiviert. Sprich eine Sektion.")
    with sr.Microphone() as quelle:
        while True:
            try:
                print("🎧 Lausche...")
                audio = recognizer.listen(quelle, timeout=8)
                befehl = recognizer.recognize_google(audio, language="de-DE").lower()
                print(f"🎤 Empfangen: {befehl}")
                verarbeite_befehl(befehl)
            except sr.UnknownValueError:
                sprich("Ich konnte dich nicht verstehen.")
            except sr.WaitTimeoutError:
                sprich("Keine Spracheingabe erkannt.")
            except KeyboardInterrupt:
                beenden()
            except Exception as fehler:
                sprich(f"Fehler erkannt: {str(fehler)}")

# 🧾 Übersicht
def zeige_sektionen():
    print("\n🔷 AUREON SEKTIONEN")
    print("1 – 🌐 Netzwerk prüfen")
    print("2 – 🔐 DNS-Status analysieren")
    print("3 – 📦 Paketliste anzeigen (Linux)")
    print("4 – 🧠 Veraltete Befehle prüfen (Prototyp)")
    print("99 – ⏹ Beenden")
    print("🛡 Sprachsteuerung aktiviert...\n")

# 🔁 Startpunkt
if __name__ == "__main__":
    print("🔵 AUREON: Missionskern V2 (KALI Root) geladen.")
    zeige_sektionen()
    sprachsteuerung()
