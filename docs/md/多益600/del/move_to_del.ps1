param(
  [Parameter(Mandatory = $true, Position = 0)]
  [string]$PathToMove,

  [string]$DelRoot = (Join-Path (Get-Location) "del")
)

$resolved = Resolve-Path -LiteralPath $PathToMove -ErrorAction Stop
New-Item -ItemType Directory -Force -Path $DelRoot | Out-Null

$itemName = Split-Path -Leaf $resolved
$destination = Join-Path $DelRoot $itemName

if (Test-Path -LiteralPath $destination) {
  $stamp = Get-Date -Format "yyyyMMdd_HHmmss"
  $suffix = [guid]::NewGuid().ToString("N").Substring(0, 6)
  $destination = Join-Path $DelRoot ($itemName + "__" + $stamp + "_" + $suffix)
}

Move-Item -LiteralPath $resolved -Destination $destination
Write-Output $destination
