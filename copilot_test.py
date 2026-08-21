import subprocess
import sys


def get_system_uptime():
    """Get system uptime using the Linux uptime command."""
    try:
        result = subprocess.run(
            ["uptime", "-p"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()

    except subprocess.CalledProcessError as error:
        print(f"Failed to get system uptime: {error}", file=sys.stderr)
        return None

    except FileNotFoundError:
        print("The 'uptime' command was not found.", file=sys.stderr)
        return None


def main():
    uptime = get_system_uptime()

    if uptime:
        print(f"System uptime: {uptime}")
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
