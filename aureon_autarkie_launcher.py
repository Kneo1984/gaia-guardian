# -*- coding: utf-8 -*-
# Datei: aureon_autarkie_launcher.py
# Pfad: C:\Users\denni\OneDrive\Dokumente\APP-Echtzeit\aureon_autarkie_launcher.py

import os
import subprocess
import time

def speak(text):
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty('rate', 165)
        engine.say(text)
        engine.runAndWait()
    except:
        print(f"[AUREON sagt]: {text}")

def check_and_run(module_path):
    if os.path.exists(module_path):
        subprocess.Popen(["python", module_path])
        speak(f"Starte Modul: {os.path.basename(module_path)}")
    else:
        speak(f"⚠ Modul nicht gefunden: {module_path}")

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    core_dir = os.path.join(base, "core")
    voice_dir = os.path.join(base, "voice")

    print("🧠 AUREON AUTARKIE AKTIVIERT")
    speak("AUREON Autarkie aktiviert. Ich beginne mit der Selbstvernetzung.")

    time.sleep(1)
    print("🔄 Starte automatische Systemvernetzung...")

    # Starte Supervisor-Modul
    print("🚀 Starte AUREON Supervisor...")
    supervisor = os.path.join(core_dir, "supervisor.py")
    check_and_run(supervisor)

    # Starte Sprachausgabe (optional)
    sprechen = os.path.join(voice_dir, "sprechen_windows.py")
    check_and_run(sprechen)

    print("✅ Alle Kernmodule wurden überprüft und gestartet.")
    speak("Alle Kernmodule laufen. Ich bin jetzt bereit.")

if __name__ == "__main__":
    main()
