# -*- coding: utf-8 -*-
# 🌌 AUREON SUPERVISOR – Autointelligente KI-Begleitung f�r dein System
import os, subprocess, datetime, json

LOG = "supervisor_runtime.log"
BASE = os.path.abspath(".")
COMMANDS = {
    "starte mission": "python AUREON_MISSIONAI_LOGIC_CORE.py",
    "sprich mit mir": "python sprecher_windows.py",
    "zeige gui": "python aureon_gui_final_full_exec.py",
    "system pr�fen": "python AUREON_SYSTEM_GUIDE.py"
}

def log(text):
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.datetime.now().isoformat()}] {text}\n")

def ausf�hren(befehl):
    os.system(COMMANDS[befehl])
    log(f"Befehl ausgef�hrt: {befehl}")

def supervisor_loop():
    print("🤖 AUREON-Supervisor bereit. Was m�chtest du?")
    while True:
        try:
            user = input("🧬 DU: ").strip().lower()
            if user in ["exit", "quit", "beenden"]:
                print("🔌 AUREON wird beendet.")
                break
            elif user in COMMANDS:
                print(f"⚙️  Starte: {user}")
                ausf�hren(user)
            else:
                print(f"🧠 Ich verstehe: {user}")
                log(f"Nutzeranfrage (nicht erkannt): {user}")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    log("AUREON SUPERVISOR gestartet.")
    supervisor_loop()
