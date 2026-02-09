# Installing GitLab on Ubuntu

## Introduction

Installing GitLab via Docker is indeed the most efficient way to get up and running on Ubuntu. Because GitLab is a "complete" DevOps platform, it contains many moving parts (PostgreSQL, Redis, Nginx, etc.); putting them in a single container simplifies maintenance significantly.

### Prerequisites & Hardware

GitLab is resource-intensive. For a smooth experience on Ubuntu, ensure your machine meets these minimums:

* **RAM:** 8 GB (GitLab *can* run on 4 GB, but it often crashes during updates).
* **CPU:** 4 Cores recommended.
* **Storage:** 10 GB+ (SSD highly recommended).

---

## Step 1: Set up the Environment

To ensure your data survives if the container is deleted or updated, you must create persistent storage directories on your Ubuntu host.

```bash
# Create a root directory for GitLab data
sudo mkdir -p /srv/gitlab

# Define an environment variable for easier commands (optional but recommended)
export GITLAB_HOME=/srv/gitlab

```

## Step 2: Deploy GitLab using Docker Compose

While you can use a single `docker run` command, using **Docker Compose** is better for long-term management because it stores your configuration in a file.

1. Create a project directory: `mkdir ~/gitlab-docker && cd ~/gitlab-docker`
2. Create a file named `docker-compose.yml`: `nano docker-compose.yml`
3. Paste the following configuration:

```yaml
version: '3.6'
services:
  web:
    image: 'gitlab/gitlab-ce:latest'
    restart: always
    hostname: 'gitlab.example.com' # Replace with your domain or local IP
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'http://gitlab.example.com' # Replace with http://your-ip
    ports:
      - '80:80'
      - '443:443'
      - '2222:22' # Map container port 22 to 2222 to avoid host SSH conflict
    volumes:
      - '$GITLAB_HOME/config:/etc/gitlab'
      - '$GITLAB_HOME/logs:/var/log/gitlab'
      - '$GITLAB_HOME/data:/var/opt/gitlab'
    shm_size: '256m'

```

> **Note on Port 22:** Ubuntu uses port 22 for its own SSH. By mapping GitLab’s SSH to **2222**, you prevent conflicts. When cloning repos later via SSH, you'll just use `ssh://git@your-ip:2222/...`.

4. Start the container:
```bash
sudo docker compose up -d

```



## Step 3: Accessing GitLab

The initialization process takes **3–5 minutes**. GitLab has to run several internal "reconfigure" scripts the first time it boots.

1. Monitor the progress: `sudo docker logs -f gitlab-docker-web-1` (Wait until you see "GitLab configured!")
2. Open your browser and go to `http://<your-server-ip>`.

## Step 4: Retrieve the Initial Admin Password

GitLab generates a random password for the `root` user upon installation.

Run this command to find it:

```bash
sudo docker exec -it gitlab-docker-web-1 grep 'Password:' /etc/gitlab/initial_root_password

```

* **Username:** `root`
* **Password:** (The string returned by the command above)

> **Important:** This password file is automatically deleted after 24 hours. Change your password immediately in the GitLab User Settings.

---

### Managing your Instance

* **Stop GitLab:** `sudo docker compose stop`
* **Update GitLab:** 

```bash
sudo docker compose pull
sudo docker compose up -d
```

