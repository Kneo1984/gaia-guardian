# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import platform
from datetime import datetime
from pathlib import Path

# === SYSTEMBASIS ===
now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
log_file = Path.home() / f"aureon_shield_log_{now}.log"

def log(msg):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}\n")
    print(msg)

# === FIREWALL AKTIVIERUNG ===
def activate_firewall():
    if platform.system() == "Windows":
        subprocess.run(["powershell", "-Command", "Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True"])
    elif platform.system() == "Linux":
        subprocess.run(["sudo", "ufw", "enable"])
    log("🔐 Firewall aktiviert.")

# === PORT- UND PROZESSÜBERWACHUNG ===
def monitor_ports():
    if platform.system() == "Windows":
        cmd = "netstat -aon"
    else:
        cmd = "ss -tuln"
    result = subprocess.getoutput(cmd)
    log("📊 Aktive Verbindungen und Ports:")
    log(result)

# === IDS-CHECKS ===
def run_ids():
    if platform.system() == "Linux":
        log("🛡️ IDS gestartet: nmap, auditd, fail2ban")
        subprocess.run(["sudo", "nmap", "-sS", "127.0.0.1"])
        subprocess.run(["sudo", "auditctl", "-s"])
        subprocess.run(["sudo", "fail2ban-client", "status"])
    else:
        log("⚠️ IDS auf Windows nicht direkt unterstützt.")

# === SYSTEM GUIDE ===
def system_guide():
    base = Path.home()
    py_files = list(base.rglob("*.py"))
    web_files = list(base.rglob("*.html")) + list(base.rglob("*.js")) + list(base.rglob("*.css"))
    model_files = list(base.rglob("*.bin")) + list(base.rglob("*.pt")) + list(base.rglob("*.onnx"))

    log("🧠 Analyse abgeschlossen – priorisierte Hinweise folgen.")
    log(f"▶️ Du hast {len(py_files)} Python-Skripte – prüfe auf alte, doppelte oder unvollständige.")
    log(f"🌐 Web-Dateien erkannt: {len(web_files)}")
    log(f"🧬 Modell-Dateien gefunden: {len(model_files)}")
    log("📌 Vorschlag: Starte ➤ AUREON_MISSIONAI_LOGIC_CORE.py oder sprecher_windows.py")

# === AUSFÜHRUNG ===
def main():
    log("💥 AUREON SHIELD MONSTER AKTIVIERT")
    activate_firewall()
    monitor_ports()
    run_ids()
    system_guide()
    log("✅ SHIELD-DURCHLAUF BEENDET.")

if __name__ == "__main__":
    main()
