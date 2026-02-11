import os
from pinecone import Pinecone
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Initialize Pinecone instance
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Replace with your index name
index_name = "langchain-test-index3"
# Replace with your name space
name_space = 'TestOne'

# Check if the index exists
if index_name not in [index.name for index in pc.list_indexes()]:
    print(f"Index '{index_name}' does not exist.")
    exit(1)

# Connect to the index
index = pc.Index(index_name)

# Fetch all vector IDs
all_vector_ids = []
for id_batch in index.list(limit=100, namespace= name_space):  # Adjust page size as needed
    all_vector_ids.extend(id_batch)
print(f"Found {len(all_vector_ids)} vector ids")

# Fetch vectors in batches and display their details
batch_size = 100  # Adjust the batch size if necessary
for i in range(0, len(all_vector_ids), batch_size):
    batch_ids = all_vector_ids[i:i + batch_size]
    print(f"Fetching batch: {batch_ids}")  # Debugging log
    
    response = index.fetch(ids=batch_ids, namespace=name_space)  
    if not response or not response.get("vectors"):  # Check if response is empty
        print(f"No data found for batch: {batch_ids}")
        continue

    for vector_id, vector_data in response["vectors"].items():  # Correct key for fetched vectors
        vector = vector_data.get("values", [])
        metadata = vector_data.get("metadata", {})
        source = metadata.get("source", "N/A")
        text = metadata.get("text", "N/A")

        print(f"Vector ID: {vector_id}")
        print(f"Vector Data: {vector}")
        print(f"Source: {source}")
        print(f"Text: {text}")
        print("-" * 40)

print("=== finished ===")
