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

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/pinecone/How%20To%20List%20Pinecone%20Vectors](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/pinecone/How%20To%20List%20Pinecone%20Vectors)
