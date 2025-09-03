# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox, ttk
import pyttsx3
import subprocess
import threading

# Sprachengine initialisieren
engine = pyttsx3.init()
engine.setProperty("rate", 160)
engine.setProperty("volume", 1.0)

def spreche(text):
    print("ğŸ§  AUREON:", text)
    engine.say(text)
    engine.runAndWait()

# Sektionen
sektionen = {
    "Sektion 1": "ğŸŒ Netzwerkprüfung",
    "Sektion 2": "ğŸ” DNS-Konfiguration prüfen",
    "Sektion 3": "ğŸ“¦ dpkg-Paketanalyse",
    "Sektion 4": "ğŸ§  Veraltete Befehle erkennen",
    "Sektion 5": "ğŸ›¡ï¸ Supervisor-Modus aktivieren",
    "Sektion 6": "ğŸ“Š Ressourcen überwachen",
    "Sektion 7": "ğŸ“ˆ Verbindung & Portanalyse",
    "Sektion 8": "ğŸ§© Integritätsprüfung & Rootkits",
    "Sektion 9": "ğŸ“œ Logging & Dialogfortsetzung",
    "Beenden": "â¹ AUREON zieht sich zurück"
}

def ausführen(sektion):
    spreche(f"Starte {sektion}")
    ausgabe = f"AUREON führt jetzt aus: {sektion}\n"
    if sektion == "Beenden":
        spreche("Mission beendet. AUREON zieht sich zurück.")
        root.destroy()
    else:
        textfeld.insert(tk.END, ausgabe)

def auswahl_aus_dropdown():
    sektion = dropdown.get()
    if sektion:
        ausführen(sektion)
    else:
        messagebox.showinfo("Hinweis", "Bitte zuerst eine Sektion auswählen.")

def spracheingabe_simuliert():
    antwort = eingabefeld.get().strip().lower()
    if "1" in antwort or "sektion 1" in antwort:
        ausführen("Sektion 1")
    elif "2" in antwort:
        ausführen("Sektion 2")
    elif "3" in antwort:
        ausführen("Sektion 3")
    elif "4" in antwort:
        ausführen("Sektion 4")
    elif "5" in antwort:
        ausführen("Sektion 5")
    elif "6" in antwort:
        ausführen("Sektion 6")
    elif "7" in antwort:
        ausführen("Sektion 7")
    elif "8" in antwort:
        ausführen("Sektion 8")
    elif "9" in antwort:
        ausführen("Sektion 9")
    elif "99" in antwort or "beenden" in antwort:
        ausführen("Beenden")
    else:
        spreche("Ich konnte den Befehl nicht zuordnen.")

# GUI
root = tk.Tk()
root.title("ğŸ§  AUREON Kontrollzentrum")
root.geometry("700x450")

title = tk.Label(root, text="ğŸ§  Wähle deine Mission:", font=("Segoe UI", 14, "bold"))
title.pack(pady=10)

dropdown = ttk.Combobox(root, values=list(sektionen.keys()), font=("Segoe UI", 12))
dropdown.pack(pady=5)

button_start = tk.Button(root, text="ğŸš€ Starte Mission", font=("Segoe UI", 12), command=auswahl_aus_dropdown)
button_start.pack(pady=10)

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

label_eingabe = tk.Label(frame_input, text="Oder sprich/schreibe (z.â€¯B. 'Sektion 1' oder '99'):", font=("Segoe UI", 10))
label_eingabe.pack(side=tk.LEFT, padx=5)

eingabefeld = tk.Entry(frame_input, font=("Segoe UI", 12), width=25)
eingabefeld.pack(side=tk.LEFT, padx=5)

button_eingabe = tk.Button(frame_input, text="ğŸ¤ Ausführen", font=("Segoe UI", 10), command=spracheingabe_simuliert)
button_eingabe.pack(side=tk.LEFT)

textfeld = tk.Text(root, height=10, font=("Consolas", 10))
textfeld.pack(pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
