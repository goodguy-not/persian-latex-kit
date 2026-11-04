# Windows compatibility wrapper. Standalone generation is the default.
param(
  [Parameter(Mandatory=$true)][string]$Destination,
  [string]$RepositoryUrl,
  [switch]$Git
)
$ErrorActionPreference = 'Stop'
$script = Join-Path $PSScriptRoot 'new-project.py'
$arguments = @($script, '--template', 'assignment', '--destination', $Destination)
if ($RepositoryUrl) { $arguments += @('--repository-url', $RepositoryUrl) }
if ($Git) { $arguments += '--git' }
if (Get-Command py -ErrorAction SilentlyContinue) {
  & py -3 @arguments
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
  & python @arguments
} else {
  throw 'Python 3 was not found. Install Python 3 to generate a project.'
}
if ($LASTEXITCODE -ne 0) { throw "Assignment project creation failed ($LASTEXITCODE)." }
