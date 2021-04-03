import requests
import json
import os
from datetime import date

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

with open('secret.json') as credentialJson:
    credentials = json.load(credentialJson)
apiKey = credentials['apikey']

with open('payload.json') as payloadJson:
    embedables = json.load(payloadJson)

if date.today().weekday() == 1:
    embed = {

        "title": embedables['title'],
        "description": embedables['description'],
        "color": embedables['color'],
        "image": {
            "url": embedables['image']['url']
        }
    }

    data = {
        "embeds": [
            embed
        ],
    }
    result = requests.post(apiKey, json=data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload Delivered Successfully, code {}.".format(result.status_code))

else:
    print("It is not Tuesday, my dude")
    exit

