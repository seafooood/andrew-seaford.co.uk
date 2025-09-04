# How To Install n8n with Langchain.js

## Introduction

In this article we are going to create a docker container that hosts n8n with Langchain.js and Pinecone depenancies. 


### Step 1 - Create Directory

```bash
mkdir n8n-langchain && cd n8n-langchain
```

### Step 2 - Create the dockerfile

Create [Dockerfile](Dockerfile) file

### Step 3 - Configure Docker Compose

Create [docker-compose.yml](docker-compose.yml) file.

### Step 4 - Start The Stack

```bash
docker-compose up -d
```

