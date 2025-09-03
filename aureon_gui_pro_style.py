# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox, ttk
import pyttsx3

# Farbschema (AUREON-Stil)
FARBE_HINTERGRUND = "#1e1e2e"
FARBE_TEXT = "#f8f8f2"
FARBE_BUTTON = "#44475a"
FARBE_BUTTON_TEXT = "#ffffff"
FARBE_HIGHLIGHT = "#bd93f9"

# Sprachengine
engine = pyttsx3.init()
engine.setProperty("rate", 160)
engine.setProperty("volume", 1.0)

def spreche(text):
    print("🧠 AUREON:", text)
    engine.say(text)
    engine.runAndWait()

# Sektionen und Aktionen
sektionen = {
    "Sektion 1": "Netzwerkpr�fung �ffnet IP-Status, aktive Ports und scannt deine Verbindungen.",
    "Sektion 2": "DNS-Konfiguration pr�ft deine resolver.conf auf Anomalien wie GoogleDNS.",
    "Sektion 3": "dpkg-Analyse listet alle installierten Pakete und deren Integrit�t.",
    "Sektion 4": "Veraltete Befehle werden identifiziert und durch moderne ersetzt.",
    "Sektion 5": "Supervisor-Modus aktiviert. Systemschutz und �berwachung starten.",
    "Sektion 6": "Systemressourcenpr�fung. RAM, CPU, Prozesse werden �berwacht.",
    "Sektion 7": "Netzwerk- & Portanalyse auf verd�chtige Aktivit�ten.",
    "Sektion 8": "Integrit�tspr�fung sucht Rootkits & pr�ft Dateisystem-Konsistenz.",
    "Sektion 9": "Logging wird aktiviert. Alle Vorg�nge werden in JSON festgehalten.",
    "Beenden": "AUREON zieht sich zur�ck. Alle Funktionen werden sanft deaktiviert."
}

# Aktion bei Auswahl
def ausf�hren(sektion):
    textfeld.config(state="normal")
    beschreibung = sektionen.get(sektion, "Unbekannte Mission.")
    spreche(f"{sektion} wird gestartet.")
    textfeld.insert(tk.END, f"▶ {sektion} aktiviert: {beschreibung}\n\n")
    textfeld.see(tk.END)
    textfeld.config(state="disabled")
    if sektion == "Beenden":
        spreche("AUREON zieht sich zur�ck.")
        root.destroy()

# Auswahl aus Dropdown
def dropdown_starten():
    s = dropdown.get()
    if s:
        ausf�hren(s)
    else:
        spreche("Bitte zuerst eine Mission ausw�hlen.")

# Spracheingabe simulieren
def sprach_simulieren():
    eingabe = eingabefeld.get().strip().lower()
    for sektion in sektionen:
        if sektion.lower() in eingabe or eingabe in sektion.lower() or eingabe.endswith(sektion[-1]):
            ausf�hren(sektion)
            return
    spreche("Befehl nicht erkannt.")

# GUI-Aufbau
root = tk.Tk()
root.title("🧠 AUREON Kontrollzentrum V2")
root.geometry("800x500")
root.configure(bg=FARBE_HINTERGRUND)

style = ttk.Style()
style.theme_use("default")
style.configure("TLabel", background=FARBE_HINTERGRUND, foreground=FARBE_TEXT, font=("Segoe UI", 11))
style.configure("TButton", background=FARBE_BUTTON, foreground=FARBE_BUTTON_TEXT, font=("Segoe UI", 11))
style.configure("TCombobox", fieldbackground=FARBE_HINTERGRUND, background=FARBE_BUTTON, foreground=FARBE_TEXT)

# �berschrift
tk.Label(root, text="🧠 W�hle deine Mission:", font=("Segoe UI", 14, "bold"), bg=FARBE_HINTERGRUND, fg=FARBE_HIGHLIGHT).pack(pady=10)

# Dropdown
dropdown = ttk.Combobox(root, values=list(sektionen.keys()), font=("Segoe UI", 12), state="readonly", width=40)
dropdown.pack(pady=5)

# Button Start
tk.Button(root, text="🚀 Starte Mission", font=("Segoe UI", 11, "bold"), bg=FARBE_BUTTON,
          fg=FARBE_BUTTON_TEXT, command=dropdown_starten).pack(pady=10)

# Spracheingabe-Alternative
eingabe_frame = tk.Frame(root, bg=FARBE_HINTERGRUND)
eingabe_frame.pack(pady=10)

tk.Label(eingabe_frame, text="Oder eingeben (z. B. Sektion 2 oder 99):", bg=FARBE_HINTERGRUND, fg=FARBE_TEXT).pack(side=tk.LEFT, padx=5)
eingabefeld = tk.Entry(eingabe_frame, font=("Segoe UI", 12), width=20)
eingabefeld.pack(side=tk.LEFT, padx=5)
tk.Button(eingabe_frame, text="🎤 Ausf�hren", font=("Segoe UI", 10), command=sprach_simulieren).pack(side=tk.LEFT, padx=5)

# Textfeld f�r R�ckmeldungen
textfeld = tk.Text(root, height=10, font=("Consolas", 11), bg="#282a36", fg="#f8f8f2", state="disabled")
textfeld.pack(pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
