import requests
import json

url = "http://140.119.163.193:8080/wise/pi/items"
headers={'content-type': 'application/json'}
payload = {
            "macAddress":"user1_testToken",
            "queue":{
            "host":"140.119.163.193",
            "ws":9001,
            "tcp":1883
            },
          }

r = requests.post(url, data=json.dumps(payload), headers=headers)
string1 = r.status_code
print(string1)
string2 = r.raise_for_status
print(string2)
print(r)
