# -*- coding: utf-8 -*-
# AUTOHEILUNG: Unicode & Logging vollständig robust
import os, json

BASE = r"C:\Users\denni\OneDrive\Dokumente\APP-Echtzeit"
MISSION_LOG = os.path.join(BASE, "mission_ai_sorted.log")
GUIDANCE_LOG = os.path.join(BASE, "aureon_guidance.log")

def list_files():
    structure = {}
    for root, dirs, files in os.walk(BASE):
        if '__pycache__' in root:
            continue
        for file in files:
            full = os.path.join(root, file)
            ext = os.path.splitext(file)[-1].lower()
            structure.setdefault(ext, []).append(full)
    return structure

def generate_guidance(file_map):
    lines = ["🔧 AUREON SYSTEM GUIDE:"]
    lines.append("🧠 Analyse abgeschlossen – priorisierte Hinweise folgen.")
    
    if ".py" in file_map:
        lines.append(f"▶️ Du hast {len(file_map['.py'])} Python-Skripte – prüfe auf alte, doppelte oder unvollständige.")
    if ".html" in file_map:
        lines.append("🌐 Web-Dateien erkannt – möchtest du daraus ein Interface generieren?")
    if "model.json" in str(file_map):
        lines.append("🧬 Modell-Dateien gefunden – KI-Kern vorhanden.")
    if "log" in file_map:
        lines.append("📜 Logs vorhanden – Analysiere letzte Systemmeldungen.")
    
    lines.append("📌 Vorschlag: Starte als Nächstes ➤ AUREON_MISSIONAI_LOGIC_CORE.py")
    lines.append("📌 Optional: Nutze sprecher_windows.py für Sprache oder GUI-Dateien für Steuerung.")

    return "\n".join(lines)

def save_guidance(text):
    try:
        with open(GUIDANCE_LOG, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"[✅] AUREON Guide gespeichert unter:\n{GUIDANCE_LOG}")
    except Exception as e:
        print(f"[❌] Fehler beim Speichern des Guides: {e}")

if __name__ == "__main__":
    files = list_files()
    guide = generate_guidance(files)
    print(guide)
    save_guidance(guide)
