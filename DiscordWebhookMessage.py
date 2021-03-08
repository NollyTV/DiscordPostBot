import requests
import json
import os
# Testing Git merges
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

with open('secret.json') as f:
    credentials = json.load(f)
apiKey = credentials['apikey']
data = {}
#data["content"] = "message content"
data["embeds"] = []
embed = {}
# Also testing merge
embed["description"] = ""
embed["title"] = ""
embed["color"] = "4289797"
data["embeds"].append(embed)

result = requests.post(apiKey, data=json.dumps(data), headers={"Content-Type": "application/json"})

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Payload Delivered Successfully, code {}.".format(result.status_code))