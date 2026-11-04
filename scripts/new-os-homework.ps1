# Standalone snapshot by default; -Git selects the previous submodule mode.
param(
  [Parameter(Mandatory=$true)][string]$Destination,
  [string]$QuestionNumber = '۱',
  [string]$AssignmentNumber,
  [string]$RepositoryUrl,
  [switch]$Git,
  [switch]$Offline,
  [string]$KitPath
)
$ErrorActionPreference = 'Stop'
$script = Join-Path $PSScriptRoot 'new-os-homework.py'
$arguments = @($script, '--destination', $Destination, '--question-number', $QuestionNumber)
if ($AssignmentNumber) { $arguments += @('--assignment-number', $AssignmentNumber) }
if ($RepositoryUrl) { $arguments += @('--repository-url', $RepositoryUrl) }
if ($Git) { $arguments += '--git' }
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
