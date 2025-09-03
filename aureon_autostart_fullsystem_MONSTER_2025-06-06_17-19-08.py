# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUREON ‐ Vollständiger Autostart‑Launcher (MONSTER Edition)
Dateiname : aureon_autostart_fullsystem_MONSTER_2025-06-06_17-19-08.py
Pfad      : C:/Users/denni/OneDrive/Dokumente/APP-Echtzeit/
Version   : 2025‑06‑22 (Root‑optimiert)

Beschreibung
============
• Prüft/legt Missions‑, Log‑ und Response‑Ordner an
• Installiert fehlende Python‑Abhängigkeiten (falls nötig)
• Erstellt Dummy‑Missionsskripte, wenn keine vorhanden
• Startet erkannte Missionsskripte im Hintergrund
• Lädt die Cosmic‑GUI

Hinweis
=======
Die automatische Installation verwendet **kein** `--user`, sodass der Code
innerhalb von Virtual‑Environments ebenso funktioniert wie systemweit.
"""

import importlib
import os
import platform
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# === BASISKONFIGURATION ======================================================
HOME = Path.home()
APP_ROOT      = HOME / "OneDrive" / "Dokumente" / "APP-Echtzeit"
MISSIONS_DIR  = APP_ROOT / "missions"
LOG_DIR       = APP_ROOT / "logs"
RESP_DIR      = APP_ROOT / "responses"
GUI_FILE      = APP_ROOT / "gui" / "aureon_gui_missions_cosmic.py"
LOG_FILE      = LOG_DIR / f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

# === HILFSFUNKTIONEN =========================================================

def log(message: str) -> None:
    """Schreibt eine Zeitmarke in die Logdatei und gibt sie auf stdout aus."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("[%H:%M:%S]")
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(f"{timestamp} {message}\n")
    print(message)


def ensure_dirs() -> None:
    """Erzeugt benötigte Verzeichnisse, falls sie fehlen."""
    for path in (MISSIONS_DIR, LOG_DIR, RESP_DIR):
        path.mkdir(parents=True, exist_ok=True)
        log(f"📁 Ordner geprüft: {path}")


def install_dependencies() -> None:
    """Installiert fehlende Abhängigkeiten ohne --user‑Flag."""
    pkgs = [
        "pyttsx3",
        "SpeechRecognition",
        "requests",
        "beautifulsoup4",
        "watchdog",
    ]
    for pkg in pkgs:
        try:
            importlib.import_module(pkg.split("==")[0].lower())
            log(f"✅ Modul bereits vorhanden: {pkg}")
        except ImportError:
            log(f"⬇️  Installiere fehlendes Modul: {pkg}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
            log(f"✅ Modul installiert: {pkg}")


def create_dummy_missions() -> None:
    """Erstellt Beispiel‑Missionsskripte, falls Missionsordner leer ist."""
    dummy_code = {
        "sektion1.py": 'print("🌐 Sektion 1 aktiviert: Netzwerküberprüfung …")',
        "sektion2.py": 'print("🛰️  Sektion 2 aktiviert: Internetverbindung …")',
        "sektion3.py": 'print("🔐 Sektion 3 aktiviert: Sicherheitseinstellungen …")',
    }
    if any(MISSIONS_DIR.iterdir()):
        log("📄 Missionsskripte bereits vorhanden – Dummy‑Erstellung übersprungen.")
        return
    for filename, code in dummy_code.items():
        filepath = MISSIONS_DIR / filename
        filepath.write_text(code, encoding="utf-8")
        log(f"⚙️  Dummy‑Skript erstellt: {filename}")


def run_missions() -> None:
    """Startet jedes Missionsskript als separaten Prozess."""
    missions = sorted(MISSIONS_DIR.glob("*.py"))
    log("🔍 Spiegelmodus aktiviert – erkannte Missionen: " + ", ".join(m.name for m in missions))
    for mission in missions:
        log(f"✨ Starte Mission: {mission.name}")
        subprocess.Popen([sys.executable, str(mission)], shell=False)


def start_gui() -> None:
    """Startet die Cosmic‑GUI, falls vorhanden."""
    if not GUI_FILE.exists():
        log("❌ GUI‑Datei nicht gefunden: " + str(GUI_FILE))
        return
    subprocess.Popen([sys.executable, str(GUI_FILE)], shell=False)
    log("🚀 GUI gestartet: AUREON Cosmic Missions")


# === HAUPTPLAN ==============================================================

def main() -> None:
    log("🧠 AUREON AUTOSTART BEGINNT…")
    ensure_dirs()
    install_dependencies()
    create_dummy_missions()
    run_missions()
    start_gui()
    log("✅ AUTOSTART‑VORGANG ABGESCHLOSSEN.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        log(f"❌ Fehler: {exc}")
