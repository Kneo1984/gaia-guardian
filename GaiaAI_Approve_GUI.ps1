# ===================================================================
# GAIA AI APPROVE GUI - Modelle in Allowlist aufnehmen
# Ersteller: KNEO + AUREON
# ===================================================================

Add-Type -AssemblyName System.Windows.Forms

# 0) Admin-Check
if (-not ([Security.Principal.WindowsPrincipal] `
    [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole(`
    [Security.Principal.WindowsBuiltInRole] "Administrator")) {
    [System.Windows.Forms.MessageBox]::Show("Bitte als Administrator starten!",
        "GAIA AI Approve", 'OK', 'Error')
    exit
}

# 1) Dateidialog öffnen
$dialog = New-Object System.Windows.Forms.OpenFileDialog
$dialog.InitialDirectory = "C:\Users\denni\OneDrive\Dokumente\GaiaAI_Models"
$dialog.Filter = "PowerShell-Skripte (*.ps1)|*.ps1"
$dialog.Title = "Wähle ein Modell zur Freigabe"

if ($dialog.ShowDialog() -eq 'OK') {
    $full = $dialog.FileName

    # 2) Hash berechnen
    $sha256 = [System.Security.Cryptography.SHA256]::Create()
    $fs = [System.IO.File]::OpenRead($full)
    $hashBytes = $sha256.ComputeHash($fs)
    $fs.Close()
    $hash = -join ($hashBytes | ForEach-Object { $_.ToString("x2") })

    # 3) Allowlist-Datei vorbereiten
    $allowFile = "C:\Users\denni\OneDrive\Dokumente\GaiaAI_Models\allowlist.json"
    if (!(Test-Path $allowFile)) {
        $init = @{ approved = @() } | ConvertTo-Json -Depth 3
        $init | Out-File $allowFile -Encoding UTF8 -Force
    }

    # 4) Bestehende Allowlist einlesen
    $allow = Get-Content $allowFile -Raw | ConvertFrom-Json
    if (-not $allow.approved) { $allow | Add-Member -MemberType NoteProperty -Name approved -Value @() }

    # 5) Prüfen ob schon drin
    $exists = $allow.approved | Where-Object { $_.path -eq $full }
    if ($exists) {
        [System.Windows.Forms.MessageBox]::Show("Modell bereits freigegeben:`n$full",
            "GAIA AI Approve", 'OK', 'Information')
    } else {
        $entry = [PSCustomObject]@{ path = $full; sha256 = $hash }
        $allow.approved += $entry
        $allow | ConvertTo-Json -Depth 3 | Out-File $allowFile -Encoding UTF8 -Force

        [System.Windows.Forms.MessageBox]::Show("Modell erfolgreich freigegeben:`n$full",
            "GAIA AI Approve", 'OK', 'Information')
    }
}
