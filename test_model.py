# -*- coding: utf-8 -*-
from gpt4all import GPT4All

print(" LEX wird geladen...")

model = GPT4All(
    model_name='gpt4all-falcon-newbpe-q4_0.gguf',
    model_path='C:/Users/denni/AppData/Local/nomic.ai/GPT4All',
    allow_download=False
)

# System-Prompt auf Deutsch setzen
antwort = model.generate(
    "Bitte antworte immer ausschlieÃŸlich auf Deutsch, hÃ¶flich und klar. Frage: Wie geht es dir?",
    max_tokens=50
)

print(" Antwort:", antwort)
