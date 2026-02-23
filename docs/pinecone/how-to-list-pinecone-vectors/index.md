---
keywords: [pinecone, list vectors, python, namespace, vector database]
---

# How To List Pinecone Vectors

In this article, we will develop a Python script that can list all of the Vectors in a Pinecone namspace. In this example, we are going to list all of the vectors in index "langchain-test-index3", namespace "TestOne".

## Procedure

1. From the terminal install Pinecone

```bash
pip install "pinecone[grpc]"
```

2. Create a text file called `.env`, within the text file create a variable `PINECONE_API_KEY =` followed by your Pinecone api key.

3. Create a python script called `pinecone-list-vectors.py`

[pinecone-list-vectors.py](pinecone-list-vectors.py)

4. Execute the python from the terminal

```bash
python pinecone-list-vectors.py
```

The script will display the vectors, source and text meta data.

![alt text](image.png)

## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/pinecone/how-to-list-pinecone-vectors](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/pinecone/how-to-list-pinecone-vectors)

## Pinecone Related Articles

- [How To Perform a Vector Search in A Postgres Database using pgvector](../../postgresql/how-to-perform-a-vector-search-in-a-postgres-database-using-pgvector/index.md)
- [Install pgvector on Ubuntu with PostgreSQL 14](../../postgresql/install-pgvector-on-ubuntu-with-postgresql-14/index.md)
- [How To Chat With Langflow From A Python Script](../../langflow/how-to-chat-with-langflow-from-a-python-script/index.md)
- [How To Enable Logging In Langflow](../../langflow/how-to-enable-logging-in-langflow/index.md)
- [How To Install Langflow on Ubuntu Using Docker](../../langflow/how-to-install-langflow-on-ubuntu-using-docker/index.md)
