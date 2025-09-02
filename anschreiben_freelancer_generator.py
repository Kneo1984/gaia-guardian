from pathlib import Path
import json
from jinja2 import Environment, FileSystemLoader

def erstelle_template(modus="freelancer"):
    """Erzeugt ein neutrales Freelancer-Anschreiben ohne Firmennamen."""
    template_dir = Path("templates")
    template_dir.mkdir(parents=True, exist_ok=True)
    template_name = f"anschreiben_template_{modus}.html"
    template_path = template_dir / template_name

    anschreiben_template = """
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <title>Freelancer – {{ name }}</title>
  <style>
    * { box-sizing: border-box; }
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      color: #333;
      line-height: 1.6;
      background-color: #f5f7fa;
    }
    .container {
      max-width: 900px;
      margin: 40px auto;
      background-color: #fff;
      display: flex;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    .sidebar {
      width: 35%;
      background-color: #1c355e;
      color: white;
      padding: 30px;
    }
    .sidebar h1 { font-size: 24px; margin-top: 0; }
    .sidebar p { margin: 5px 0; }
    .main-content {
      width: 65%;
      padding: 40px;
    }
    .main-content h2 { font-size: 20px; margin-top: 0; }
    .signatur { margin-top: 50px; }
  </style>
</head>
<body>
  <div class="container">
    <div class="sidebar">
      <h1>{{ name }}</h1>
      <p>{{ kontakt.adresse }}</p>
      <p>{{ kontakt.email }}</p>
    </div>
    <div class="main-content">
      <h2>Angebot für Data-Analytics- und BI-Projekte</h2>
      <p>{{ anschreiben | safe }}</p>
      <div class="signatur">
        Mit freundlichen Grüßen,<br><br>
        {{ name }}
      </div>
    </div>
  </div>
</body>
</html>
"""
    template_path.write_text(anschreiben_template.strip(), encoding="utf-8")
    print(f"✔ Template ({modus}) gespeichert unter: {template_path}")

def render_template(modus="freelancer"):
    """Rendert ein neutrales Freelancer-Anschreiben mit deiner Handschrift."""
    daten_pfad = "data/data_dennis.json"
    template_name = f"anschreiben_template_{modus}.html"
    output_pfad = f"output/anschreiben_dennis_maier_{modus}.html"

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template(template_name)

    with open(daten_pfad, "r", encoding="utf-8") as f:
        daten = json.load(f)

    anschreiben_text = """
ich bin als freiberuflicher Data Analyst tätig und unterstütze Organisationen dabei, aus Daten strukturierte Erkenntnisse zu gewinnen. Mein Fokus liegt auf der Entwicklung klarer Dashboards, effizienter Datenmodelle und automatisierter Analysen – immer mit dem Ziel, Informationen verständlich und zugänglich zu machen.

Ich bringe Erfahrung in SQL, Power BI, Python und ETL-Prozessen mit und habe in verschiedenen Rollen analytisch, technisch und operativ gearbeitet. Mein Arbeitsstil ist strukturiert, vorausschauend und lösungsorientiert. Dabei lege ich großen Wert auf Kommunikation und ein gutes Verständnis für die fachlichen Anforderungen meiner Auftraggeber.

Wenn Sie Unterstützung bei datengetriebenen Fragestellungen benötigen – projektbezogen oder kontinuierlich – freue ich mich über Ihre Nachricht.
"""

    html = template.render(
        name=daten["name"],
        kontakt=daten["kontakt"],
        anschreiben=anschreiben_text,
        modus=modus
    )

    Path("output").mkdir(parents=True, exist_ok=True)
    with open(output_pfad, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✔ Freelancer-Anschreiben generiert unter: {output_pfad}")

if __name__ == "__main__":
    erstelle_template("freelancer")
    render_template("freelancer")
