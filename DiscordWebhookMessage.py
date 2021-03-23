import requests
import json
import os
from datetime import date

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

with open('secret.test.json') as f:
    credentials = json.load(f)
apiKey = credentials['apikey']
data = {}
#data["content"] = "message content"
data["embeds"] = []
embed = {}

if date.today().weekday() == 1:
    embed["description"] = "This is a threat"
    embed["title"] = "Update your lootsheet, jackalope"
    embed["color"] = "15105570"
    data["embeds"].append(embed)
    result = requests.post(apiKey, data=json.dumps(data), headers={"Content-Type": "application/json"})
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload Delivered Successfully, code {}.".format(result.status_code))
    
else:
    print("It is not Tuesday, my dude")
    exit