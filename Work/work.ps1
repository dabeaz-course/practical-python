param([string]$Command)

switch ($Command) {
    "env" {
        python -m venv env
        iex $PSScriptRoot\env\Scripts\Activate.ps1
        pip install -r $PSScriptRoot\requirements.txt
    }
    "test" {
        pytest $PSScriptRoot -q
    }
    "test:watch" {
        ptw $PSScriptRoot -- -q
    }
    default {
        Write-Error "Command '$Command' not found."
    }
}