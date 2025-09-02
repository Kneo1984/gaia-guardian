# ===================================================================
# GAIA AI START GUI - Startet alle freigegebenen Modelle
# Ersteller: KNEO + AUREON
# ===================================================================

Add-Type -AssemblyName System.Windows.Forms

# 0) Admin-Check
if (-not ([Security.Principal.WindowsPrincipal] `
    [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole(`
    [Security.Principal.WindowsBuiltInRole] "Administrator")) {
    [System.Windows.Forms.MessageBox]::Show("Bitte als Administrator starten!",
        "GAIA AI START", 'OK', 'Error')
    exit
}

# 1) Allowlist laden
$allowFile = "C:\Users\denni\OneDrive\Dokumente\GaiaAI_Models\allowlist.json"
if (!(Test-Path $allowFile)) {
    [System.Windows.Forms.MessageBox]::Show("Keine Allowlist gefunden!",
        "GAIA AI START", 'OK', 'Error')
    exit
}

$allow = Get-Content $allowFile -Raw | ConvertFrom-Json
if (-not $allow.approved -or $allow.approved.Count -eq 0) {
    [System.Windows.Forms.MessageBox]::Show("Keine Modelle freigegeben.",
        "GAIA AI START", 'OK', 'Information')
    exit
}

# 2) Modelle starten
$started = @()
foreach ($model in $allow.approved) {
    if (Test-Path $model.path) {
        try {
            Start-Process powershell.exe -ArgumentList "-ExecutionPolicy Bypass -File `"$($model.path)`"" -WindowStyle Minimized
            $started += $model.path
        } catch {
            [System.Windows.Forms.MessageBox]::Show("Fehler beim Starten von: $($model.path)",
                "GAIA AI START", 'OK', 'Error')
        }
    }
}

# 3) Meldung
if ($started.Count -gt 0) {
    $msg = "Gestartete Modelle:`n" + ($started -join "`n")
    [System.Windows.Forms.MessageBox]::Show($msg, "GAIA AI START", 'OK', 'Information')
} else {
    [System.Windows.Forms.MessageBox]::Show("Keine Modelle gestartet.",
        "GAIA AI START", 'OK', 'Warning')
}
