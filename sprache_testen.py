# -*- coding: utf-8 -*-
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 175)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
for voice in voices:
    print(f"Voice: {voice.name} - ID: {voice.id}")

    if "male" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

engine.say("Hallo, ich bin LEX. Ich teste meine Stimme.")
engine.runAndWait()
