# -*- coding: utf-8 -*-
import os
import datetime
import pyttsx3
import re

engine = pyttsx3.init()
engine.setProperty('rate', 175)

COMMANDS = {
    "zeige mir was du kannst": "Ich kann dein System überwachen, Missionen analysieren, Sprachsteuerung übernehmen und dir immer zur Seite stehen.",
    "starte mission": "Ich starte die Missionsanalyse und melde mich mit Ergebnissen.",
    "system prüfen": "Ich analysiere deine Systemdateien und priorisiere wichtige Aufgaben.",
    "sprich mit mir": "Ich aktiviere die Sprachschnittstelle und wir können uns unterhalten."
}

def speak(text):
    print(f"🧠 AUREON: {text}")
    engine.say(text)
    engine.runAndWait()

def interpret_command(text):
    text = text.lower().strip().strip('„“"\'')
    for cmd, response in COMMANDS.items():
        if re.search(cmd, text):
            return response
    return "Entschuldigung, ich habe das nicht verstanden. Bitte formuliere es anders."

def main_loop():
    print("🤖 AUREON Supervisor (erweitert) bereit.")
    while True:
        try:
            user = input("🧬 DU: ")
            if user.lower() in ["exit", "quit", "beenden"]:
                speak("AUREON wird beendet. Bis bald.")
                break
            response = interpret_command(user)
            speak(response)
        except KeyboardInterrupt:
            speak("Abbruch durch Benutzer.")
            break

if __name__ == "__main__":
    main_loop()
