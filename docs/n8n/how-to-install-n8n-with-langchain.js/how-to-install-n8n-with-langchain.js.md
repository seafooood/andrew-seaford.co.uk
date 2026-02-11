# How To Install n8n with Langchain.js

## Introduction

In this article we are going to create a docker container that hosts n8n with Langchain.js and Pinecone depenancies. 


### Step 1 - Create Directory

```bash
mkdir n8n-langchain && cd n8n-langchain
```

### Step 2 - Create the dockerfile

```dockerfile
FROM n8nio/n8n:latest

USER root

# Install build tools required for npm packages
RUN apk add --no-cache bash python3 make g++

# Create a dedicated folder for extra node dependencies
WORKDIR /usr/local/lib/node_deps
RUN npm init -y \
    && npm install --no-audit --no-fund langchain openai @pinecone-database/pinecone

# Add shim file
COPY langchain-shim.js /usr/local/lib/node_deps/

# Tell Node.js (and n8n) where to find these modules
ENV NODE_PATH=/usr/local/lib/node_deps/node_modules

# Reset working dir back to n8n's default
WORKDIR /data

USER node
```

### Step 3 - Configure Docker Compose

Create [docker-compose.yml](docker-compose.yml) file.

### Step 4 - Start The Stack

```bash
docker-compose up -d
```



## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/n8n/how-to-install-n8n-with-langchain.js](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/n8n/how-to-install-n8n-with-langchain.js)
