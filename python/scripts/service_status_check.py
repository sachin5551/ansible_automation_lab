#!/usr/bin/env python3

import subprocess
import sys
import json

def check_service(service):
    try:
        result = subprocess.run(
            ["systemctl", "is-active", service],
            capture_output=True,
            text=True,
            check=True,
        )
        return {"service": service, "status": result.stdout.strip()}
    except subprocess.CalledProcessError:
        return {"service": service, "status": "not running"}

def main():
    if len(sys.argv) !=2:
        print(json.dumps({"error": "Usage: service_status_check.py <service_name>"}))
        sys.exit(1)


    service = sys.argv[1]
    result = check_service(service)
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()
