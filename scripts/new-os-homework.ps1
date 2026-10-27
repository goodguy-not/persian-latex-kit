# Default: Git submodule from the library's origin remote (central updates).
# Example: .\scripts\new-os-homework.ps1 -Destination "E:\uni\os\HW2_Q1" -QuestionNumber "۱" -AssignmentNumber "۲"
# Explicit offline option: add -Offline (a frozen style snapshot).
param(
  [Parameter(Mandatory=$true)][string]$Destination,
  [string]$QuestionNumber = '۱',
  [string]$AssignmentNumber = '۲',
  [string]$RepositoryUrl,
  [switch]$Offline,
  [string]$KitPath
)
$ErrorActionPreference = 'Stop'
$script = Join-Path $PSScriptRoot 'new-os-homework.py'
$arguments = @($script, '--destination', $Destination, '--question-number', $QuestionNumber, '--assignment-number', $AssignmentNumber)
if ($RepositoryUrl) { $arguments += @('--repository-url', $RepositoryUrl) }
if ($Offline) { $arguments += '--offline' }
if ($KitPath) { $arguments += @('--kit-path', $KitPath) }
if (Get-Command py -ErrorAction SilentlyContinue) {
  & py -3 @arguments
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
  & python @arguments
} else {
  throw 'Python 3 was not found. Install Python 3 before running this wrapper.'
}
if ($LASTEXITCODE -ne 0) { throw "OS project creation failed ($LASTEXITCODE)." }
