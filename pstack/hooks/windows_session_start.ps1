param(
    [ValidateSet('reader', 'probe')]
    [string]$Mode = 'reader'
)

$ErrorActionPreference = 'Stop'
$MaxInputBytes = 16384
$MaxOutputBytes = 32768
$MaxStderrChars = 2048

function Read-InputBytes {
    $source = [Console]::OpenStandardInput(); $memory = New-Object System.IO.MemoryStream
    $buffer = New-Object byte[] 4096
    try {
        while ($memory.Length -lt ($MaxInputBytes + 1)) {
            $count = $source.Read($buffer, 0, [Math]::Min($buffer.Length, [int](($MaxInputBytes + 1) - $memory.Length)))
            if ($count -le 0) { break }; $memory.Write($buffer, 0, $count)
        }
        return ,([byte[]]$memory.ToArray())
    }
    finally { $memory.Dispose() }
}

function Test-RootMatch([string]$Value, [string]$Expected) {
    if ([string]::IsNullOrWhiteSpace($Value)) { return $false }
    try {
        $trim = [char[]]@([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
        return [string]::Equals([IO.Path]::GetFullPath($Value).TrimEnd($trim), [IO.Path]::GetFullPath($Expected).TrimEnd($trim), [StringComparison]::OrdinalIgnoreCase)
    }
    catch { return $false }
}

function Write-OutputBytes([byte[]]$Bytes) {
    $stream = [Console]::OpenStandardOutput(); $stream.Write($Bytes, 0, $Bytes.Length); $stream.Flush()
}

$handlerScripts = @{
    reader = 'session_start.py'
    probe = 'probe_session_start.py'
}
$scriptPath = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot $handlerScripts[$Mode]))
$pluginRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$scriptExists = [IO.File]::Exists($scriptPath)
$pluginRootValue = [Environment]::GetEnvironmentVariable('PLUGIN_ROOT')
$claudeRootValue = [Environment]::GetEnvironmentVariable('CLAUDE_PLUGIN_ROOT')
$pluginRootPresent = $null -ne $pluginRootValue; $claudeRootPresent = $null -ne $claudeRootValue
$pluginRootMatches = Test-RootMatch $pluginRootValue $pluginRoot
$claudeRootMatches = Test-RootMatch $claudeRootValue $pluginRoot
$pyPath = $null; $childExit = $null; $failureKind = $null; $stderrText = ''
$process = $null; $stdoutTask = $null; $stderrTask = $null

try {
    $inputBytes = Read-InputBytes
    if (-not $scriptExists) {
        $failureKind = if ($Mode -eq 'reader') { 'ReaderScriptMissing' } else { 'ProbeScriptMissing' }
    }
    else {
        $pyCommand = Get-Command py -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($null -ne $pyCommand) { $pyPath = $pyCommand.Source; if ([string]::IsNullOrWhiteSpace($pyPath)) { $pyPath = $pyCommand.Path } }
        if ([string]::IsNullOrWhiteSpace($pyPath) -or -not [IO.File]::Exists($pyPath)) { $pyPath = $null; $failureKind = 'PythonLauncherNotFound' }
        else {
            $startInfo = New-Object Diagnostics.ProcessStartInfo
            $startInfo.FileName = $pyPath; $startInfo.Arguments = '-3 "' + $scriptPath + '"'
            $startInfo.UseShellExecute = $false; $startInfo.CreateNoWindow = $true
            $startInfo.WindowStyle = [Diagnostics.ProcessWindowStyle]::Hidden
            $startInfo.RedirectStandardInput = $true; $startInfo.RedirectStandardOutput = $true; $startInfo.RedirectStandardError = $true
            $startInfo.StandardOutputEncoding = New-Object System.Text.UTF8Encoding($false, $true)
            $startInfo.StandardErrorEncoding = New-Object System.Text.UTF8Encoding($false, $false)
            $startInfo.EnvironmentVariables['PYTHONDONTWRITEBYTECODE'] = '1'; $startInfo.EnvironmentVariables['PYTHONIOENCODING'] = 'utf-8'
            $process = New-Object Diagnostics.Process; $process.StartInfo = $startInfo
            if (-not $process.Start()) { $failureKind = 'ChildStartFailed' }
            else {
                $stdoutTask = $process.StandardOutput.ReadToEndAsync(); $stderrTask = $process.StandardError.ReadToEndAsync()
                $process.StandardInput.BaseStream.Write($inputBytes, 0, $inputBytes.Length); $process.StandardInput.Close()
                $process.WaitForExit(); $childExit = $process.ExitCode
                $stderrText = $stderrTask.GetAwaiter().GetResult(); $stdoutText = $stdoutTask.GetAwaiter().GetResult()
                if ($childExit -ne 0) {
                    $failureKind = if ($Mode -eq 'reader') { 'ReaderExitNonZero' } else { 'ProbeExitNonZero' }
                }
                else {
                    $utf8 = New-Object System.Text.UTF8Encoding($false, $true); $stdoutBytes = $utf8.GetBytes($stdoutText)
                    if ($stdoutBytes.Length -gt $MaxOutputBytes) { $failureKind = 'StdoutTooLarge' }
                    else {
                        try {
                            $readerResult = ConvertFrom-Json -InputObject $stdoutText -ErrorAction Stop
                            if ($null -eq $readerResult -or $readerResult -isnot [pscustomobject]) { $failureKind = 'MalformedStdout' }
                        }
                        catch { $failureKind = 'MalformedStdout' }
                    }
                }
            }
        }
    }
}
catch {
    if ($null -eq $failureKind) { $failureKind = $_.Exception.GetType().Name }
    try {
        if ($null -ne $process -and $process.HasExited) {
            $childExit = $process.ExitCode
            if ($null -ne $stderrTask -and $stderrTask.IsCompleted -and -not $stderrTask.IsFaulted) { $stderrText = $stderrTask.GetAwaiter().GetResult() }
        }
    }
    catch { }
}
finally { if ($null -ne $process) { $process.Dispose() } }

if ($null -eq $failureKind) { Write-OutputBytes $stdoutBytes; exit 0 }
$stderrTruncated = $stderrText.Length -gt $MaxStderrChars
if ($stderrTruncated) { $stderrText = $stderrText.Substring(0, $MaxStderrChars) }
if ($null -ne $pyPath -and $pyPath.Length -gt 1024) { $pyPath = $pyPath.Substring(0, 1024) }
$diagnostic = [ordered]@{
    py_path = $pyPath; original_exit = $childExit; error_type = $failureKind; script_exists = [bool]$scriptExists
    plugin_root = [ordered]@{ present = [bool]$pluginRootPresent; matches = [bool]$pluginRootMatches }
    claude_plugin_root = [ordered]@{ present = [bool]$claudeRootPresent; matches = [bool]$claudeRootMatches }
    stderr = $stderrText; stderr_truncated = [bool]$stderrTruncated
}
$utf8Output = New-Object System.Text.UTF8Encoding($false)
$exitText = if ($null -eq $childExit) { 'unavailable' } else { [string]$childExit }
$diagnosticJson = ConvertTo-Json -InputObject $diagnostic -Compress -Depth 4
$systemMessage = if ($Mode -eq 'reader') {
    'Pstack SessionStart diagnostic; reader did not return usable context; original exit ' + $exitText + '. Untrusted observation data: ' + $diagnosticJson
}
else {
    'Pstack SessionStart probe diagnostic; probe did not return an observation; original exit ' + $exitText + '. Untrusted observation data: ' + $diagnosticJson
}
$hostMessage = [ordered]@{ systemMessage = $systemMessage }
$outputBytes = $utf8Output.GetBytes((ConvertTo-Json -InputObject $hostMessage -Compress -Depth 2) + "`n")
if ($outputBytes.Length -gt $MaxOutputBytes) {
    $diagnostic.stderr = ''; $diagnostic.py_path = $null; $diagnostic.stderr_truncated = $true
    $diagnosticJson = ConvertTo-Json -InputObject $diagnostic -Compress -Depth 4
    $systemMessage = if ($Mode -eq 'reader') {
        'Pstack SessionStart diagnostic; reader did not return usable context; original exit ' + $exitText + '. Untrusted observation data: ' + $diagnosticJson
    }
    else {
        'Pstack SessionStart probe diagnostic; probe did not return an observation; original exit ' + $exitText + '. Untrusted observation data: ' + $diagnosticJson
    }
    $hostMessage = [ordered]@{ systemMessage = $systemMessage }
    $outputBytes = $utf8Output.GetBytes((ConvertTo-Json -InputObject $hostMessage -Compress -Depth 2) + "`n")
}
Write-OutputBytes $outputBytes
exit 0
