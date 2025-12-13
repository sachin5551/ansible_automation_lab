#!/usr/bin/env python3
import json

data = {"name": "Sachin", "status": "success"}
print(json.dumps(data, indent=4))

json_str = '{"name": "Sachin", "score": 100}'
data = json.loads(json_str)
print(data["score"])

