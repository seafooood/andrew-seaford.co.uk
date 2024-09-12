+++
title = 'How To Install Dify AI Locally On Ubuntu'
date = 2024-09-12T08:42:04+01:00
draft = false
+++

In this tutorial, I’ll walk you through the process of installing Dify on an Ubuntu system. In this tutorial we will execute Dify using the Docker image.

## Install Process

- Clone the Dify source code to your local machine

    ```bash
    git clone https://github.com/langgenius/dify.git
    ```

- Change directory

    ```bash
    cd dify/docker
    ```

- Copy environment setting file

    ```bash
    cp .env.example .env
    ```

- Start docker

    ```bash
    docker compose up -d
    ```
