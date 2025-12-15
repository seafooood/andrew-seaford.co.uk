# How To Install Langflow on Ubuntu Using Docker

## Introduction

Install Langflow on Ubuntu using docker.


## Procedure

1. Installer docker

```bash
sudo apt-get install docker.io
```

2. Run latest container from langflow

```bash
docker run -it --rm -p 7860:7860 langflowai/langflow:latest
```

![run docker](image.png)

3. Navigate to http://127.0.0.1:7860

## References

https://hub.docker.com/r/langflowai/langflow