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
