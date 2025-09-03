# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

data = [
    (1, "„Sektion 1“", "🌐 Netzwerkprüfung (IP, aktive Verbindungen)"),
    (2, "„Sektion 2“", "🔐 DNS-Konfiguration prüfen (Leak, Google DNS etc.)"),
    (3, "„Sektion 3“", "📦 dpkg-Paketanalyse (installierte Pakete, Sicherheitsstatus)"),
    (4, "„Sektion 4“", "🧠 Veraltete Befehle erkennen & Alternativen anzeigen"),
    (5, "„Sektion 5“", "🛡️ Supervisor-Modus aktivieren und Systemüberwachung starten"),
    (6, "„Sektion 6“", "📊 Ressourcen- und Prozessanalyse mit psutil"),
    (7, "„Sektion 7“", "📈 Analyse verdächtiger Verbindungen & Ports"),
    (8, "„Sektion 8“", "🧩 Integritätsprüfung und Rootkit-Scanner"),
    (9, "„Sektion 9“", "📜 JSON-Logging & Sprachdialog fortsetzen"),
    (99, "„Beenden“", "⏹ AUREON zieht sich zurück")
]

root = tk.Tk()
root.title("AUREON – Interaktive Sektionen")

tree = ttk.Treeview(root, columns=("Nummer", "Sprachbefehl", "Funktion"), show="headings")
tree.heading("Nummer", text="Nummer")
tree.heading("Sprachbefehl", text="Sprachbefehl")
tree.heading("Funktion", text="Funktion")

for eintrag in data:
    tree.insert("", tk.END, values=eintrag)

tree.pack(expand=True, fill=tk.BOTH)
root.mainloop()
