#!/usr/bin/env python3

import json
import subprocess

def run_command(cmd):   #cmd is expected to be a list of command arguments, e.g. ["df", "-h"]
    """Run a shell command and return output or error."""
    try:                # try block to catch errors when running shell command
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {"success": True, "output": result.stdout.strip()}
    except subprocess.CalledProcessError as e:            #Catches errors if the command fails.
        return {"success": False, "error": e.stderr.strip()}

def get_disk_usage():
    """Returns disk usage (automation-friendly format)."""
    return run_command(["df", "-h"])

def get_uptime():
    """Returns system uptime."""
    return run_command(["uptime", "-p"])

def main():                     #Defines the main function where the program logic lives.
    data = {                    #Starts creating a dictionary named data
        "disk_usage": get_disk_usage(),
        "uptime": get_uptime()
    }

    print(json.dumps(data, indent=4))  #Converts the data dictionary into pretty-printed JSON and ident=4 makes it human-readable.

if __name__ == "__main__":      #Checks if the script is being run directly, not imported as a module.
    main()

