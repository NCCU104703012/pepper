import requests
import json

url = "http://140.119.163.193:8080/wise/login"
headers={'content-type': 'application/json'}
payload = {
           "user":"user1",
           "password":"123456"
          }

r = requests.post(url, data=json.dumps(payload), headers=headers)
string1 = r.status_code
print(string1)
string2 = r.raise_for_status
print(string2)
print(r.json())
