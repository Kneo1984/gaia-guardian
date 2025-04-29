# 🌍 Gaia Guardian

**Gaia Guardian** ist ein intelligentes Umweltüberwachungssystem, das kritische Umweltdaten erkennt, automatisch protokolliert und Warnungen über Telegram und E-Mail versendet. Es wurde für ethische, friedliche und zukunftsgerichtete Anwendungen im Sinne der Erde und ihrer Lebewesen entwickelt.

---

## ✨ Funktionen

- 🌱 Echtzeit-Analyse von Umweltdaten (Toxizität, Sauerstoffgehalt, Mikroplastik, Ölverschmutzung)
- 📊 Automatisches Logging kritischer Ereignisse
- 📩 Alarmierung per E-Mail und Telegram-Bot
- 🔐 Umweltsensitive Konfiguration über `.env` (nicht öffentlich sichtbar)
- 🤖 Vollständig Python-basiert, erweiterbar & modular
- 🔁 Dauerbetrieb über Watchdog-Loop möglich

---

## 📁 Projektstruktur
📦 GaiaGuardian/ ├── gaia_guardian_dashboard.py # Hauptskript mit Logik & Automatisierung ├── gaia_guardian_core.ipynb # Jupyter-Analyse & Dokumentation ├── gaia_guardian_log.txt # Log-Datei (automatisch erzeugt) ├── .env.example # Beispiel für Konfigurationsdatei ├── .gitignore # schützt sensible Daten └── README.md # diese Datei


---

## ⚙️ Einrichtung

1. Klone das Repository:
   ```bash
   git clone https://github.com/Kneo1984/gaia-guardian.git


Erstelle eine .env Datei nach dem Beispiel in .env.example
und trage deine Zugangsdaten für E-Mail und Telegram ein.

Installiere Abhängigkeiten:

bash
Kopieren
Bearbeiten
pip install -r requirements.txt
Starte den Wächter:

bash
Kopieren
Bearbeiten
python gaia_guardian_dashboard.py


## ✍️ Urheber

Dieses Projekt wurde entwickelt von **Dennis Maier (Kneo1984)**  
© 2025 – Alle Rechte am Ursprungscode vorbehalten.  
Freigegeben unter der MIT-Lizenz für offene und ethische Nutzung.

