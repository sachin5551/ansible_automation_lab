#!/usr/bin/env python3

import yaml
import json

with open("demo.txt", "w") as f:
    f.write("This is line 1")


with open("demo.txt", "a") as f:
    f.write("\nThis is line 2 appended")

with open("demo.txt", "r") as f:
    text_data = f.read()
    print("\n---- Text File Content ----")
    print(text_data)

sample_yaml = {
        "project": "automation-demo",
        "owner": "Sachin Vashishtha",
        "servers": ["web01", "web02"]
    }

#Write yaml
with open("sample.yml", "w") as f:
    yaml.dump(sample_yaml, f)       #Convert Python object to yaml format

with open("sample.yml", "r") as f:
    yaml_data = yaml.safe_load(f)   #this converts YAML file to python object

print("\n--- YAML Content ---")
print(json.dumps(yaml_data, indent=4))

