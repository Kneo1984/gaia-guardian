from pathlib import Path
import json
from jinja2 import Environment, FileSystemLoader

def erstelle_template(modus="neutral"):
    """Speichert das HTML-Grundtemplate (je nach Modus)."""
    template_dir = Path("templates")
    template_dir.mkdir(parents=True, exist_ok=True)
    template_name = f"anschreiben_template_{modus}.html"
    template_path = template_dir / template_name

    anschreiben_template = """
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <title>Anschreiben – {{ name }}</title>
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
      <h2>Bewerbung um die Stelle als {{ bewerbung.stelle }} bei {{ bewerbung.unternehmen }} <span style="font-size:14px; color:gray;">({{ modus }})</span></h2>
      <p>
      {% if bewerbung.ansprechpartner %}
        Sehr geehrter {{ bewerbung.ansprechpartner }},
      {% else %}
        Sehr geehrtes Team,
      {% endif %}
      </p>
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

def render_template(modus="neutral"):
    """Rendert das HTML-Anschreiben mit JSON-Daten."""
    daten_pfad = "data/daten_partner_dennis.json"

    template_name = f"anschreiben_template_{modus}.html"
    output_pfad = f"output/anschreiben_dennis_maier_{modus}.html"

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template(template_name)

    with open(daten_pfad, "r", encoding="utf-8") as f:
        daten = json.load(f)

    html = template.render(
        name=daten["name"],
        kontakt=daten["kontakt"],
        bewerbung=daten["bewerbung"],
        anschreiben=daten["anschreiben"],
        modus=modus
    )

    Path("output").mkdir(parents=True, exist_ok=True)
    with open(output_pfad, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✔ HTML-Datei ({modus}) generiert unter: {output_pfad}")

if __name__ == "__main__":
    modus = "neutral"
    erstelle_template(modus)
    render_template(modus)
