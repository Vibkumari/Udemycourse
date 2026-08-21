# Udemycourse
# System Uptime Script

## Description

This project contains a Python script that displays the system uptime.

The initial version of the script was generated with the help of GitHub Copilot.

## Copilot Experience

GitHub Copilot was used to generate and improve the system uptime script.

Copilot suggested improvements related to security, reliability, and exception handling.

## Changes Made

The script was modified to:

- Replace `os.popen()` with `subprocess.run()`.
- Use an argument list instead of executing a shell command directly.
- Add exception handling for command execution failures.
- Handle the case where the `uptime` command is unavailable.
- Return appropriate exit codes.
- Improve code readability using separate functions.

Using `subprocess.run()` without `shell=True` helps avoid unnecessary shell execution and makes command execution safer.

## Testing

The script was tested by running:

```bash
python3 copilot_test.py
