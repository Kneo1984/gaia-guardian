# ===================================================================
# GAIA AI START TEST - Lädt und startet alle freigegebenen Modelle
# Ersteller: KNEO + AUREON
# ===================================================================

Write-Host ">>> GAIA AI START TEST <<<" -ForegroundColor Cyan

$DocRoot   = "C:\Users\denni\OneDrive\Dokumente"
$ModelsDir = Join-Path $DocRoot "GaiaAI_Models"
$Allowlist = Join-Path $ModelsDir "allowlist.json"

if (!(Test-Path $Allowlist)) {
    Write-Error "Keine Allowlist gefunden: $Allowlist"
    exit 1
}

# Allowlist laden
$allow = Get-Content -Raw -Path $Allowlist | ConvertFrom-Json

if (-not $allow.approved) {
    Write-Error "Allowlist ist leer oder fehlerhaft."
    exit 1
}

# Cleanup: ungültige Einträge rausfiltern
$allow.approved = @($allow.approved | Where-Object { $_ -and $_.path })

Write-Host "Gefundene Modelle: $($allow.approved.Count)" -ForegroundColor White

foreach ($model in $allow.approved) {
    if (-not (Test-Path $model.path)) {
        Write-Warning "Datei fehlt: $($model.path)"
        continue
    }

    Write-Host "Starte Modell: $($model.path)" -ForegroundColor Green
    try {
        powershell -ExecutionPolicy Bypass -File $model.path
    } catch {
        Write-Host "Fehler beim Start von $($model.path): $_" -ForegroundColor Red
    }
}

Write-Host ">>> Alle freigegebenen Modelle wurden verarbeitet." -ForegroundColor Yellow
