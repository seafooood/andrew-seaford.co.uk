import requests
import json

# Set your API key here
API_KEY = "your_api_key_here"

url = f"http://192.168.127.153:4891/api/v2/completions"
headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}

data = {
    "prompt": "This is a test prompt",
    "max_length": 100,
    "temperature": 0.5
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    print(json.dumps(result, indent=4))
else:
    print(f"Error: {response.text}")


