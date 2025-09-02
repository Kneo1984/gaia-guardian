# ===================================================================
# GaiaAI_Approve.ps1  nimmt ein Modell in die Allowlist auf (SHA256)
# Nutzung:
#   powershell -ExecutionPolicy Bypass -File ".\GaiaAI_Approve.ps1" -Path "C:\Users\denni\OneDrive\Dokumente\GaiaAI_Models\mein.ps1"
# ===================================================================

param(
    [Parameter(Mandatory=$true)][string]$Path
)

$DocRoot   = "C:\Users\denni\OneDrive\Dokumente"
$ModelsDir = Join-Path $DocRoot "GaiaAI_Models"
$Allowlist = Join-Path $ModelsDir "allowlist.json"

if (-not (Test-Path $Path)) { Write-Error "Datei nicht gefunden: $Path"; exit 1 }
$full = (Resolve-Path $Path).Path

# Sicherheitszaun: nur innerhalb des Models-Ordners
if (-not ($full.ToLower().StartsWith((Resolve-Path $ModelsDir).Path.ToLower()))) {
    Write-Error "Nur Dateien innerhalb von $ModelsDir sind zulässig."
    exit 1
}

function Get-Hash($p) { (Get-FileHash -Algorithm SHA256 -Path $p).Hash.ToLower() }

# --- 1) Allowlist laden oder neu erstellen ---
if (-not (Test-Path $Allowlist)) {
    Write-Host ">>> Neue Allowlist wird erstellt: $Allowlist" -ForegroundColor Yellow
    @{ approved = @() } | ConvertTo-Json -Depth 3 | Out-File $Allowlist -Encoding UTF8 -Force
}

try {
    $allow = Get-Content -Path $Allowlist -Raw | ConvertFrom-Json
} catch {
    Write-Warning "Allowlist defekt – wird neu erstellt."
    $allow = @{ approved = @() }
}

# Falls approved fehlt oder NULL ist
if (-not $allow.PSObject.Properties.Name.Contains("approved") -or $null -eq $allow.approved) {
    $allow | Add-Member -NotePropertyName approved -NotePropertyValue @() -Force
}

# --- 2) Hash berechnen und prüfen ---
$hash = Get-Hash $full
$existing = $allow.approved | Where-Object { $_.path.ToLower() -eq $full.ToLower() }

if ($existing) {
    $existing.sha256 = $hash
    Write-Host ">>> Hash aktualisiert für: $full" -ForegroundColor Magenta
} else {
    $entry = [PSCustomObject]@{ path=$full; sha256=$hash }
    $allow.approved += $entry
    Write-Host ">>> Neues Modell freigegeben: $full" -ForegroundColor Green
}

$allow.updated = (Get-Date).ToString("s")
$allow | ConvertTo-Json -Depth 5 | Out-File -FilePath $Allowlist -Encoding UTF8 -Force

Write-Host "    SHA256: $hash" -ForegroundColor White
Write-Host "    Allowlist: $Allowlist" -ForegroundColor White
