# ===================================================================
# GAIA AI START - Lädt und startet alle freigegebenen Modelle
# Ersteller: KNEO + AUREON
# ===================================================================

Write-Host ">>> GAIA AI START <<<" -ForegroundColor Cyan

$DocRoot   = "C:\Users\denni\OneDrive\Dokumente"
$ModelsDir = Join-Path $DocRoot "GaiaAI_Models"
$Allowlist = Join-Path $ModelsDir "allowlist.json"
$LogDir    = Join-Path $DocRoot "GAIA_Guardian_Logs"

if (!(Test-Path $LogDir)) { New-Item -ItemType Directory -Path $LogDir | Out-Null }
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$logFile   = Join-Path $LogDir "GaiaAI_Start_$timestamp.txt"

# --- 1) Allowlist prüfen ---
if (!(Test-Path $Allowlist)) {
    Write-Error "Keine Allowlist gefunden: $Allowlist"
    exit 1
}

$allow = Get-Content -Raw -Path $Allowlist | ConvertFrom-Json

if (-not $allow.approved) {
    Write-Error "Allowlist ist leer oder fehlerhaft."
    exit 1
}

# Cleanup
$allow.approved = @($allow.approved | Where-Object { $_ -and $_.path })

"=== GAIA AI START ($timestamp) ===" | Out-File $logFile
"Gefundene Modelle: $($allow.approved.Count)" | Out-File $logFile -Append

# --- 2) Modelle starten ---
foreach ($model in $allow.approved) {
    if (-not (Test-Path $model.path)) {
        $msg = "Fehlt: $($model.path)"
        Write-Warning $msg
        $msg | Out-File $logFile -Append
        continue
    }

    $msg = "Starte Modell: $($model.path)"
    Write-Host $msg -ForegroundColor Green
    $msg | Out-File $logFile -Append

    try {
        # Jedes Modell in eigenem Prozess starten
        Start-Process powershell.exe -ArgumentList "-ExecutionPolicy Bypass -File `"$($model.path)`""
    } catch {
        $err = "Fehler bei $($model.path): $_"
        Write-Host $err -ForegroundColor Red
        $err | Out-File $logFile -Append
    }
}

"=== Fertig. Alle freigegebenen Modelle gestartet. ===" | Out-File $logFile -Append
Write-Host ">>> Alle Modelle gestartet. Log gespeichert: $logFile" -ForegroundColor Yellow
