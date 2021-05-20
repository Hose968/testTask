import json
from urllib.request import urlopen
import requests

json_string = [{
    "tltie": "first",
    "title": "No First is here",
    "description": "description 1",
    "iocs": {
      "ip": "91.222.154.88",
      "asn": "AS49561",
      "skip": "I'm from England"
    }
  },
  {
    "title": "second",
    "description": "description 2",
    "iocs": {
      "asn": "AS29559",
      "ip": "195.177.208.1",
      "comment": "Our IP?"
    },
    "check": "not checked"
  },
  {
    "title": "third",
    "descripting": "description 3",
    "description": "hacker",
    "iocs": {
      "data": "check this one",
      "ip": "93.115.21.119",
      "lp": "176.36.15.129",
      "asn": "AS202448"
    }
  },
  {
    "title": "fourth",
    "description": "Ho-ho-ho",
    "descripton": "description 4",
    "iocs": {
      "asn": "AS43139",
      "ip": "178.158.224.3"
    }
  },
  {
    "title": "fifth",
    "description": "description 5",
    "iocs": {
      "ip": "8.8.8.8",
      "data": "google",
      "asn": "AS12025"
    }
  }]
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

for i in range(len(json_string)):
    response = urlopen(f"http://ipinfo.io/{json_string[i]['iocs']['ip']}/json")
    data_resp = json.load(response)
    if data_resp['country'] == 'UA':
      response1 = requests.post('http://93.115.21.119/api/case', json={"title": "test","description": "test"}, headers={'Authorization': 'Bearer ' + auth_token})
      res=response1.json()
      response2 = requests.post(f'http://93.115.21.119/api/case/{res["id"]}/ioc',json={"type":"IP","value":f"{json_string[i]['iocs']['ip']}"},headers={'Authorization': 'Bearer ' + auth_token})
      print(response2.json())


