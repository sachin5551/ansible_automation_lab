#!/usr/bin/env python3

import json
import subprocess

def run_command(cmd):
    """Run a shell command and return output or error."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {"success": True, "output": result.stdout.strip()}
    except subprocess.CalledProcessError as e:
        return {"success": False, "error": e.stderr.strip()}

def get_disk_usage():
    """Returns disk usage (automation-friendly format)."""
    return run_command(["df", "-h"])

def get_uptime():
    """Returns system uptime."""
    return run_command(["uptime", "-p"])

def main():
    data = {
        "disk_usage": get_disk_usage(),
        "uptime": get_uptime()
    }

    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()

