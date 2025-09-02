from jinja2 import Environment, FileSystemLoader
import json
import os

# Optional: Sicherstellen, dass Verzeichnisse stimmen
basis_pfad = os.path.dirname(__file__)
json_pfad = os.path.join(basis_pfad, "data", "daten_partner_dennis.json")

template_name = "anschreiben_template.html"
output_pfad = "output/anschreiben_dennis_maier.html"

# Eigener Filter für Zeilenumbrüche im HTML
def nl2br(value):
    return value.replace("\n", "<br>\n")

# Template-Umgebung vorbereiten (Ordner "templates" muss existieren)
env = Environment(loader=FileSystemLoader("templates"))
env.filters['nl2br'] = nl2br

# JSON-Daten laden (zuerst prüfen, ob Datei überhaupt existiert)
if not os.path.exists(json_pfad):
    raise FileNotFoundError(f"❌ JSON-Datei nicht gefunden: {json_pfad}")

with open(json_pfad, encoding="utf-8") as f:
    daten = json.load(f)  # Lade alle Bewerbungsdaten als Dictionary

# Template laden und mit Daten befüllen
template = env.get_template(template_name)
output = template.render(
    name=daten["name"],
    kontakt=daten["kontakt"],
    anschreiben=daten["anschreiben"],
    bewerbung=daten["bewerbung"]
)

# Ausgabeordner prüfen oder erstellen
os.makedirs(os.path.dirname(output_pfad), exist_ok=True)

# HTML-Datei speichern
with open(output_pfad, "w", encoding="utf-8") as f:
    f.write(output)

print("✅ Anschreiben erfolgreich erstellt!")
