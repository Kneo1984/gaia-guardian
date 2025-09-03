# -*- coding: utf-8 -*-
import os
import time
import json
from pathlib import Path
import platform

# === BASISPFAD automatisch bestimmen ===
if platform.system() == "Windows":
    basis = Path("C:/")
else:
    basis = Path.home()

# === AUSSCHLÜSSE (optional) ===
AUSSCHLUSS_PFADE = ["venv", ".cache", "AppData", "__pycache__"]

# === OPTIONALE DB-BEREINIGUNG ===
for file in basis.rglob("*.db"):
    try:
        file.unlink()
        print(f"🗑️  Entfernt: {file}")
    except Exception:
        continue

# === SCAN-FUNKTION mit Fortschrittsanzeige ===
def scan_verzeichnisse():
    print("📡 Starte AUREON-Speicheranalyse...\n")
    dateiliste = []

    # Schritt 1: Gesamtzahl berechnen
    gesamt = 0
    for root, _, files in os.walk(basis):
        if any(ignored in root for ignored in AUSSCHLUSS_PFADE):
            continue
        gesamt += len(files)

    if gesamt == 0:
        print("⚠️  Keine Dateien gefunden. Pfad prüfen.")
        return

    # Schritt 2: Datei-Scan mit Fortschritt
    zaehler = 0
    for root, dirs, files in os.walk(basis):
        if any(ignored in root for ignored in AUSSCHLUSS_PFADE):
            continue

        for datei in files:
            try:
                pfad = Path(root) / datei
                stat = pfad.stat()

                eintrag = {
                    "Dateiname": datei,
                    "Pfad": str(pfad),
                    "Größe": f"{stat.st_size} Bytes",
                    "Zeit": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat.st_mtime))
                }
                dateiliste.append(eintrag)

                zaehler += 1
                prozent = (zaehler / gesamt) * 100
                print(f"🔄 [{zaehler}/{gesamt}] {eintrag['Pfad']} ({eintrag['Größe']}) - {prozent:.1f}%")

            except Exception:
                continue

    # Schritt 3: Ergebnisse speichern
    result_path = Path(__file__).resolve().parent / "scan_result.json"
    with open(result_path, "w", encoding="utf-8") as f:
        json.dump(dateiliste, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Scan abgeschlossen: {len(dateiliste)} Dateien erkannt.")
    print(f"💾 Ergebnisse gespeichert in: {result_path}")

# === HAUPTSTART ===
if __name__ == "__main__":
    scan_verzeichnisse()
