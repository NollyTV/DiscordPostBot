import requests
import json
import os
from datetime import date

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

with open('secret.json') as f:
    credentials = json.load(f)
apiKey = credentials['apikey']

if date.today().weekday() == 1:
    embed = {
        "title": "Update your lootsheet, jackalope",
        "color": "15105570",
        "image": {
            "url": "https://i.imgur.com/yeEnrQU.jpeg"
        }
    }

    data = {
        "embeds": [
            embed
        ],
    }
    headers = {
        "Content-Type": "application/json"
    }
    result = requests.post(apiKey, json=data, headers=headers)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload Delivered Successfully, code {}.".format(result.status_code))

else:
    print("It is not Tuesday, my dude")
    exit

