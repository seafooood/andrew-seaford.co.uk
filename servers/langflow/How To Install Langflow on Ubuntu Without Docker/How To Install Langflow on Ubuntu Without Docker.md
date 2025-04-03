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

## 4. Create a Systemd Service

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

Now Langflow should be running on your Ubuntu machine without Docker on port 8000. Using a web browser navigate to <http:\\<server ip address>:8080>
