import requests
import json

url = 'http://192.168.127.146/v1/workflows/run'
headers = {
    'Authorization': 'Bearer app-9wDu4ap97skBFe2kt37MWD4S',
    'Content-Type': 'application/json'
}

# Define the payload
payload = {
    "inputs": {"a": "0", "b": "2", "c": "3"},
    "response_mode": "streaming",
    "user": "harry"
}

# Make the POST request and stream the response
response = requests.post(url, headers=headers, data=json.dumps(payload), stream=True)

# Check if the response status is OK
collected_output = None
if response.status_code == 200:
    # Process each line in the stream
    for line in response.iter_lines():
        # Filter out keep-alive new lines
        if line:
            # Decode the line (from bytes to string)
            decoded_line = line.decode('utf-8')
            
            # Check if the line starts with "data: " and then parse the JSON
            if decoded_line.startswith("data: "):
                # Strip the "data: " prefix and parse the JSON data
                json_data = decoded_line[len("data: "):]
                try:
                    # Convert the string to a JSON object
                    parsed_json = json.loads(json_data)
                    print(json.dumps(parsed_json, indent=4))


                    # Check if 'outputs' is in the JSON data and store it
                    if 'outputs' in parsed_json.get('data', {}):
                        outputs = parsed_json['data']['outputs']
                        collected_output = outputs
                    
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)

# Display the collected outputs at the end
if collected_output:
    print("\nCollected Outputs:")
    print(json.dumps(collected_output, indent=4))
else:
    print("No outputs were found in the stream.")
