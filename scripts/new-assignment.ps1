# Run from the library's root directory or supply this script's full path.
# E.g. .\scripts\new-assignment.ps1 -Destination "E:\uni\assignments\course-hw1" -RepositoryUrl "https://github.com/USER/persian-latex-kit.git"
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
  git init -b main
  if ($LASTEXITCODE -ne 0) { throw 'Git init failed' }
  git submodule add $RepositoryUrl vendor/persian-latex-kit
  if ($LASTEXITCODE -ne 0) { throw 'Git submodule add failed. Make sure the library repository is accessible and the latest template changes were pushed.' }
  Write-Host 'Project is ready. Open main.tex in TeXstudio and compile with XeLaTeX.'
  Write-Host 'Edit config/metadata.tex and questions/question01.tex first.'
} finally { Pop-Location }
