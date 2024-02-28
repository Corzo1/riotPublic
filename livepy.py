import requests
import json
x = requests.get(
    "https://127.0.0.1:2999/liveclientdata/activeplayer", verify=False)

with open("swagger.json", "w") as f:
    parsed = json.loads(x.text)
    f.write(json.dumps(parsed, indent=4, sort_keys=False))
print(x.text)
