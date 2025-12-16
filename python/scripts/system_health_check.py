#!/usr/bin/env python3

import subprocess
import json

def run_cmd(cmd):
    try:
        result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True,
            )
        return {"success": True, "output": result.stdout.strip()}
    except subprocess.CalledProcessError as e:
        return {"success": False, "error": e.stderr.strip()}


def main():
#   import pdb; pdb.set_trace()
    data = {
        "disk": run_cmd(["df", "-h"]),
        "memory": run_cmd(["free", "-m"]),
        "uptime": run_cmd(["uptime", "-p"]),
    }

    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()
