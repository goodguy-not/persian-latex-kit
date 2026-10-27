# Run from the kit root. Example:
# .\scripts\new-lab-report.ps1 -Destination "E:\uni\lab\experiment-2" -RepositoryUrl "https://github.com/USER/persian-latex-kit.git"
param(
  [Parameter(Mandatory=$true)][string]$Destination,
  [Parameter(Mandatory=$true)][string]$RepositoryUrl
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
if (Test-Path $Destination) { throw "Destination already exists: $Destination" }
New-Item -ItemType Directory -Force -Path $Destination | Out-Null
Copy-Item (Join-Path $root 'templates\lab-report\*') $Destination -Recurse -Force
Copy-Item (Join-Path $root 'templates\lab-report\.gitignore') $Destination -Force
Push-Location $Destination
try {
  git init -b main
  if ($LASTEXITCODE -ne 0) { throw 'Git init failed' }
  git submodule add $RepositoryUrl vendor/persian-latex-kit
  if ($LASTEXITCODE -ne 0) { throw 'Git submodule add failed; check connectivity and the published library version.' }
  Write-Host 'Ready: edit config/metadata.tex and sections/*.tex; compile main.tex twice with XeLaTeX.'
} finally { Pop-Location }
