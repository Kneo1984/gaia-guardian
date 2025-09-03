# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
import pyttsx3

# Farben & Stil
BG = "#1e1e2e"
FG = "#f8f8f2"
BTN_BG = "#44475a"
BTN_TXT = "#ffffff"
HIGHLIGHT = "#bd93f9"
TEXT_BG = "#282a36"
TEXT_FG = "#f8f8f2"

# Sprachmodul
engine = pyttsx3.init()
engine.setProperty("rate", 160)
engine.setProperty("volume", 1.0)

def spreche(text):
    print("ðŸ§  AUREON:", text)
    engine.say(text)
    engine.runAndWait()

# Sektionen + Beschreibung
sektionen = {
    "Sektion 1": "Netzwerkprüfung öffnet IP-Status, aktive Ports und scannt deine Verbindungen.",
    "Sektion 2": "DNS-Konfiguration prüft deine resolver.conf auf Anomalien wie GoogleDNS.",
    "Sektion 3": "dpkg-Analyse listet alle installierten Pakete und deren Integrität.",
    "Sektion 4": "Veraltete Befehle werden identifiziert und durch moderne ersetzt.",
    "Sektion 5": "Supervisor-Modus aktiviert. Systemschutz und Überwachung starten.",
    "Sektion 6": "Systemressourcenprüfung. RAM, CPU, Prozesse werden überwacht.",
    "Sektion 7": "Netzwerk- & Portanalyse auf verdächtige Aktivitäten.",
    "Sektion 8": "Integritätsprüfung sucht Rootkits & prüft Dateisystem-Konsistenz.",
    "Sektion 9": "Logging wird aktiviert. Alle Vorgänge werden in JSON festgehalten.",
    "Beenden": "AUREON zieht sich zurück. Alle Funktionen werden sanft deaktiviert."
}

# Ausführung
def ausführen(sektion):
    beschreibung = sektionen.get(sektion, "Unbekannte Mission.")
    meldung = f"â–¶ {sektion} aktiviert: {beschreibung}"
    textfeld.config(state="normal")
    textfeld.insert(tk.END, meldung + "\n")
    textfeld.see(tk.END)
    textfeld.config(state="disabled")
    spreche(meldung)
    if sektion == "Beenden":
        root.destroy()

# Auswahlfunktion
def starte_dropdown():
    s = dropdown.get()
    if s:
        ausführen(s)
    else:
        spreche("Bitte eine Mission auswählen.")

def starte_eingabe():
    cmd = eingabefeld.get().strip().lower()
    for sektion in sektionen:
        if sektion.lower() in cmd or cmd in sektion.lower() or cmd in sektion[-2:]:
            ausführen(sektion)
            return
    spreche("Befehl unklar oder Sektion nicht erkannt.")

# GUI
root = tk.Tk()
root.title("ðŸ§  AUREON Kontrollzentrum FINAL")
root.geometry("860x520")
root.configure(bg=BG)

# Style
style = ttk.Style()
style.theme_use("default")
style.configure("TLabel", background=BG, foreground=FG)
style.configure("TButton", background=BTN_BG, foreground=BTN_TXT)
style.configure("TCombobox", fieldbackground=BG, background=BTN_BG, foreground=FG)

# UI Elemente
tk.Label(root, text="ðŸ§  Wähle deine Mission:", font=("Segoe UI", 14, "bold"), bg=BG, fg=HIGHLIGHT).pack(pady=10)

dropdown = ttk.Combobox(root, values=list(sektionen.keys()), font=("Segoe UI", 12), state="readonly", width=45)
dropdown.pack(pady=5)

tk.Button(root, text="ðŸš€ Starte Mission", font=("Segoe UI", 11, "bold"), bg=BTN_BG, fg=BTN_TXT, command=starte_dropdown).pack(pady=10)

eingabe_frame = tk.Frame(root, bg=BG)
eingabe_frame.pack(pady=5)

tk.Label(eingabe_frame, text="Oder eingeben (z.â€¯B. Sektion 3 oder 99):", bg=BG, fg=FG).pack(side=tk.LEFT, padx=5)
eingabefeld = tk.Entry(eingabe_frame, font=("Segoe UI", 12), width=20)
eingabefeld.pack(side=tk.LEFT, padx=5)
tk.Button(eingabe_frame, text="ðŸŽ¤ Ausführen", font=("Segoe UI", 10), command=starte_eingabe).pack(side=tk.LEFT, padx=5)

textfeld = tk.Text(root, height=14, font=("Consolas", 10), bg=TEXT_BG, fg=TEXT_FG, state="disabled")
textfeld.pack(pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
