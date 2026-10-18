param(
  [Parameter(Mandatory=$true)][string]$Destination,
  [Parameter(Mandatory=$true)][string]$RepositoryUrl
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
if (Test-Path $Destination) { throw "Destination already exists: $Destination" }
New-Item -ItemType Directory -Force -Path $Destination | Out-Null
Copy-Item (Join-Path $root 'templates\assignment\*') $Destination -Recurse -Force
Copy-Item (Join-Path $root 'templates\assignment\.gitignore') $Destination -Force
Push-Location $Destination
try {
  git init
  if ($LASTEXITCODE -ne 0) { throw 'Git init failed' }
  git submodule add $RepositoryUrl vendor/persian-latex-kit
  if ($LASTEXITCODE -ne 0) { throw 'Git submodule add failed' }
  Write-Host 'Done! Open main.tex in TeXstudio and build with XeLaTeX.'
} finally { Pop-Location }
