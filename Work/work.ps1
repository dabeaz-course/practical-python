param([string]$Command)

switch ($Command) {
    "venv" {
        & python -m venv .venv
        & $PSScriptRoot\.venv\Scripts\Activate.ps1
        & pip install -r $PSScriptRoot\requirements.txt
    }
    "test" {
        & pytest $PSScriptRoot -q
    }
    "test:watch" {
        & ptw $PSScriptRoot -- -q
    }
    "lint" {
        & ruff check .
    }
    "lint:fix" {
        & ruff check . --fix
    }
    default {
        Write-Error "Command '$Command' not found."
    }
}