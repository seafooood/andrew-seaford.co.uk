# How To Find Pinecone Index Dimensions

In this article we will develop a Python script that can display the name and dimension size of indexes defined in Pinecone.

## Procedure

1. From the terminal install Pinecone

```bash
pip install "pinecone[grpc]"
```

2. Create a text file called `.env`, within the text file create a variable `PINECONE_API_KEY =` followed by your Pinecone api key.

3. Create a python script called `pinecone-list-indexes.py`.


4. Execute the python from the terminal

```bash
python pinecone-list-indexes.py
```

The output will display the index name, dimension and configured meta data.

![alt text](image.png)


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/pinecone/How%20To%20Find%20Index%20Dimensions](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/pinecone/How%20To%20Find%20Index%20Dimensions)
