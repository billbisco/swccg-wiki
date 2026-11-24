# Install the no-token unpushed-work guard as a Windows scheduled task on manpc.
# Run as the desktop user that owns C:\Users\gythe\.grok. Refs swccg-guild/work#1323.
$ErrorActionPreference = "Stop"
$ops = "C:\Users\gythe\.grok\swccg-ops"
$log = Join-Path $ops "logs"
$dest = Join-Path $ops "unpushed_work_guard.py"
$srcCandidates = @(
    "C:\Users\gythe\.grok\swccg-wiki\ops\unpushed_work_guard.py",
    (Join-Path $PSScriptRoot "unpushed_work_guard.py")
)
New-Item -ItemType Directory -Force -Path $ops, $log | Out-Null
$src = $srcCandidates | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $src) { throw "unpushed_work_guard.py not found" }
if ((Resolve-Path $src).Path -ne (Resolve-Path $dest -ErrorAction SilentlyContinue).Path) {
    Copy-Item -Force $src $dest
}
# Keep a local copy of the Git helper imported as tools/backup_git.py
$tools = Join-Path $ops "tools"
New-Item -ItemType Directory -Force -Path $tools | Out-Null
$gitSrcCandidates = @(
    "C:\Users\gythe\.grok\swccg-wiki\tools\backup_git.py",
    (Join-Path $PSScriptRoot "..\tools\backup_git.py")
)
$gitSrc = $gitSrcCandidates | Where-Object { Test-Path $_ } | Select-Object -First 1
if ($gitSrc) { Copy-Item -Force $gitSrc (Join-Path $tools "backup_git.py") }

$py = (Get-Command py -ErrorAction Stop).Source
$taskName = "SWCCG Unpushed Wiki Backup Guard"
$arg = "-3 `"$dest`" --log-dir `"$log`""
$action = New-ScheduledTaskAction -Execute $py -Argument $arg -WorkingDirectory $ops
$t1 = New-ScheduledTaskTrigger -Daily -At 9:00AM
$t2 = New-ScheduledTaskTrigger -Daily -At 9:00PM
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $t1,$t2 -Principal $principal -Settings $settings -Force | Out-Null
Get-ScheduledTask -TaskName $taskName | Format-List TaskName, State, TaskPath
Get-ScheduledTask -TaskName $taskName | Get-ScheduledTaskInfo | Format-List LastRunTime, NextRunTime, LastTaskResult
