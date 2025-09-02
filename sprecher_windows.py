# -*- coding: utf-8 -*-
# sprecher_windows.py
import pyttsx3

engine = pyttsx3.init()
engine.say("AUREON spricht mit dir aus Windows.")
engine.runAndWait()
