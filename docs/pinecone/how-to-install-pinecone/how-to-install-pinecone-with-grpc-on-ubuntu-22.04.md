---
keywords: [pinecone, grpc, installation, ubuntu, vector database]
---

# How To Install Pinecone with GRPC on Ubuntu 22.04

## Introduction

gRPC (Google Remote Procedure Call) is an open-source remote procedure call (RPC) framework created by Google. It allows different services to communicate with each other across networks in a fast, efficient, and language-agnostic way. gRPC uses HTTP/2 for transport, Protocol Buffers (protobufs) for data serialization.

In the context of pinecone[grpc], installing Pinecone with gRPC enables faster, more efficient communication between your code and the Pinecone API, which can improve performance when handling large-scale or real-time machine-learning data.

## Installation Procedure

1. From the terminal install pinecone using pip

```bash
pip install "pinecone[grpc]"
```

2. Confirm that Pinecone has been successfully installed by running a simple command in the terminal to check if the Python package is accessible. If Pinecone is installed successfully, you should see the version number of the Pinecone library printed in the terminal.

If it’s not installed, you’ll get an ImportError, which means you'll need to try installing it again.

```bash
python -c "import pinecone; print(pinecone.__version__)"
```

![success](image.png)


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/pinecone/how-to-install-pinecone](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/pinecone/how-to-install-pinecone)
