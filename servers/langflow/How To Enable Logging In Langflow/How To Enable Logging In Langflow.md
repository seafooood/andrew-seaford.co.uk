# How To Enable Logging In Langflow

## Introduction

The Langflow API contains a endpoint for retrieving log messages. This endpoint requires log retrieval to be enabled in your Langflow application. For more information about the logging end point see <https://docs.langflow.org/api-reference-api-examples#logs>

This article assumes Langflow has been installed using procedure <../How To Install Langflow on Ubuntu Without Docker/How To Install Langflow on Ubuntu Without Docker.md>.

## Component Code

To test the logging we are going to use a simple component called Andrew1 that outputs the log message "Starting Andrew1".

```python
from langflow.custom import Component
from langflow.io import MessageTextInput, Output
from langflow.schema.message import Message
import logging

class CombineTextComponent(Component):
    display_name = "Andrew1"
    description = "Concatenate two text sources into a single text chunk using a specified delimiter."
    icon = "merge"
    name = "CombineText"

    inputs = [
        MessageTextInput(
            name="text1",
            display_name="First Text",
            info="The first text input to concatenate.",
        )
    ]

    outputs = [
        Output(display_name="Combined Text", name="combined_text", method="combine_texts"),
    ]

    def combine_texts(self) -> Message:
        logger.info("Starting Andrew1")  # Log message here
        self.status = self.text1
        return self.text1
```

## Enable Logging

### Step 1. Create the .env File

Since Langflow is running as a systemd service, environment variables need to be stored in a .env file and loaded correctly. Navigate to Langflow’s working directory you can place the .env file here, or wherever Langflow is installed. In this example, we are going to place the file at `/home/harry/.env`.

Create or edit the .env file:

```bash
sudo nano /home/harry/.env
```

Add the following lines:

```ini
LANGFLOW_ENABLE_LOG_RETRIEVAL=true
LANGFLOW_LOG_RETRIEVER_BUFFER_SIZE=10000
LANGFLOW_LOG_LEVEL=DEBUG
```

Save and exit (CTRL+X, then Y, then ENTER).

### Step 2. Update the Systemd Service File

Modify the Langflow service file to load the .env file.

Open the service file:

```bash
sudo nano /etc/systemd/system/langflow.service
```

Update the [Service] section to load the .env file, note that the file contains an absolute path to the environment file:

```ini
[Unit]
Description=Langflow Service
After=network.target

[Service]
User=harry
EnvironmentFile=/home/harry/.env
ExecStart=/usr/bin/python3 -m langflow run --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
Save and exit (CTRL+X, then Y, then ENTER).
```

### Step 3. Reload Systemd and Restart Langflow

After modifying the service file, reload systemd and restart Langflow:

```bash
sudo systemctl daemon-reload
sudo systemctl restart langflow.service
```

Check if the service is running correctly:

```bash
sudo systemctl status langflow.service
```

### Step 4. Verify Logs API

Now, try the log retrieval API, this assumes that Langflow server ip address is 192.168.127.129, running on port 8000.

```bash
curl -X GET "http://192.168.127.129:8000/logs?lines_before=0&lines_after=0&timestamp=0" -H "accept: application/json"
```

The curl request should display the log messages from Langflow.

```log
curl -X GET "http://192.168.127.129:8000/logs?lines_before=0&lines_after=0&timestamp=0" -H "accept: application/json"
{"1742721898813":"2025-03-23T09:24:58.813357+0000 DEBUG Building Prompt\n","1742721898818":"2025-03-23T09:24:58.818555+0000 DEBUG Building Chat Input\n","1742721898837":"2025-03-23T09:24:58.837079+0000 DEBUG Building OpenAI\n","1742721898877":"2025-03-23T09:24:58.877983+0000 DEBUG Logged transaction: c4bce45a-a560-4ec6-9f15-c075a83c5a15\n","1742721898896":"2025-03-23T09:24:58.896524+0000 DEBUG Logged transaction: 0f2c5da3-25c1-40f4-b11d-acd43d88bb64\n","1742721904746":"2025-03-23T09:25:04.746088+0000 DEBUG Building Andrew1\n","1742721904752":"2025-03-23T09:25:04.752512+0000 INFO Starting Andrew1\n","1742721904764":"2025-03-23T09:25:04.764104+0000 DEBUG Building Chat Output\n","1742721904783":"2025-03-23T09:25:04.783589+0000 DEBUG Logged transaction: 5e97f4d6-1e0e-4dd2-bfb4-cc3a902828bc\n","1742721904806":"2025-03-23T09:25:04.806003+0000 DEBUG Logged transaction: 31519031-5eb1-4b25-8ab3-4f400f237bb4\n"}
```

## Clean Output

The text output from the curl is a little difficult to read. The following python script outputs the logs in a json format.

```python
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
```

Execute the python script

```bash
python.exe langflow-logs.py
```

Python script output

```log
{
    "1742721898896": "2025-03-23T09:24:58.896524+0000 DEBUG Logged transaction: 0f2c5da3-25c1-40f4-b11d-acd43d88bb64\n",
    "1742721904746": "2025-03-23T09:25:04.746088+0000 DEBUG Building Andrew1\n",
    "1742721904752": "2025-03-23T09:25:04.752512+0000 INFO Starting Andrew1\n",
    "1742721904764": "2025-03-23T09:25:04.764104+0000 DEBUG Building Chat Output\n",
    "1742721904783": "2025-03-23T09:25:04.783589+0000 DEBUG Logged transaction: 5e97f4d6-1e0e-4dd2-bfb4-cc3a902828bc\n",
    "1742721904806": "2025-03-23T09:25:04.806003+0000 DEBUG Logged transaction: 31519031-5eb1-4b25-8ab3-4f400f237bb4\n",
    "1742721941158": "2025-03-23T09:25:41.158379+0000 DEBUG Job queue for job_id 46779e99-5636-49a0-91bc-d5638f1f228a marked for cleanup.\n",
    "1742721941165": "2025-03-23T09:25:41.165339+0000 INFO Commencing cleanup for job_id 46779e99-5636-49a0-91bc-d5638f1f228a\n",
    "1742721941170": "2025-03-23T09:25:41.170521+0000 DEBUG Removed 1 items from queue for job_id 46779e99-5636-49a0-91bc-d5638f1f228a\n",
    "1742721941175": "2025-03-23T09:25:41.175944+0000 INFO Cleanup successful for job_id 46779e99-5636-49a0-91bc-d5638f1f228a: resources have been released.\n"
}
```
