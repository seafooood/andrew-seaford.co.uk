import requests
import json

url = "http://192.168.127.129:8000/logs?lines_before=0&lines_after=0&timestamp=0"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    logs = response.json()
    print(json.dumps(logs, indent=4))
else:
    print("Failed to retrieve logs:", response.text)
