#!/usr/bin/env python3

import json
import subprocess

name = "Sachin"
role = "Automation Engineer"

info = {
    "name": name,
    "role": role,
    "skills": ["Linux", "Ansible", "Python"]
}


print("Employee Info:")
print(json.dumps(info, indent=4))

cmd_result = subprocess.run(["uptime", "-p"], capture_output=True, text=True)
print("\nSystem Uptime:")
print(cmd_result.stdout.strip())

