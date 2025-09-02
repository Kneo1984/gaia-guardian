from jinja2 import Environment, FileSystemLoader
import json
from pathlib import Path

# Absoluter Pfad zum Projektverzeichnis
projektpfad = Path(r"C:\Users\denni\OneDrive\Dokumente\Lebenslauf\Lebenslau_Generator")

# Lade die JSON-Daten aus dem richtigen data-Verzeichnis
with open(projektpfad / "data" / "daten_partner_dennis.json", encoding="utf-8") as f:
    daten = json.load(f)

# Jinja2-Umgebung auf das templates-Verzeichnis ausrichten
env = Environment(loader=FileSystemLoader(projektpfad / "templates"))
template = env.get_template("lebenslauf_template.html")

# HTML aus Template + JSON-Daten erzeugen
output = template.render(daten)

# Ausgabeordner "output" vorbereiten
output_ordner = projektpfad / "output"
output_ordner.mkdir(exist_ok=True)

# HTML-Datei speichern im output-Verzeichnis
output_datei = output_ordner / "lebenslauf_dennis_maier.html"
with open(output_datei, "w", encoding="utf-8") as f:
    f.write(output)

print(f"✅ Lebenslauf erfolgreich erstellt unter: {output_datei}")
