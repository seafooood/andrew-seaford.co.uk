---
keywords: [langflow, ubuntu, installation, python, manual setup]
---

# How To Install Langflow on Ubuntu Without Docker

Installing Langflow on an Ubuntu machine without Docker requires setting up installing dependencies manually. Follow these steps:

## 1. Update System Packages

```bash
sudo apt update && sudo apt upgrade -y
```

## 2. Install Dependencies

Langflow requires Python and other system libraries.

```bash
sudo apt install python3 python3-venv python3-pip build-essential -y
```

## 3. Install Langflow

```bash
pip install --break-system-packages langflow
```

## 4. Create setting file

Create an envioment file

```bash
sudo nano .env
```

Add the settings to the file

```ini
LANGFLOW_ENABLE_LOG_RETRIEVAL=true
LANGFLOW_LOG_RETRIEVER_BUFFER_SIZE=10000
LANGFLOW_LOG_LEVEL=DEBUG
LANGFLOW_AUTO_LOGIN=True
```

## 5. Create a Systemd Service

To run Langflow as a background service:

Create a new service file:

```bash
sudo nano /etc/systemd/system/langflow.service
```

Add the following content:

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
```

(Replace username `harry` with your actual username if different.)

Reload systemd and enable the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable langflow
sudo systemctl start langflow
```

Check the service status:

```bash
sudo systemctl status langflow
```

Now Langflow should be running on your Ubuntu machine without Docker on port 8000. Using a web browser navigate to `http://<server_ip_address>:8000`


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/langflow/how-to-install-langflow-on-ubuntu-without-docker](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/langflow/how-to-install-langflow-on-ubuntu-without-docker)

## Langflow Related Articles

- [How To Chat With Langflow From A Python Script](../how-to-chat-with-langflow-from-a-python-script/index.md)
- [How To Enable Logging In Langflow](../how-to-enable-logging-in-langflow/index.md)
- [How To Install Langflow on Ubuntu Using Docker](../how-to-install-langflow-on-ubuntu-using-docker/index.md)
- [A Guide to Removing Unused Docker Images on Ubuntu](../../docker/a-guide-to-removing-unused-docker-images-on-ubuntu/index.md)
- [Containerize An Inno Installed Application](../../docker/containerize-an-inno-installed-application/index.md)
