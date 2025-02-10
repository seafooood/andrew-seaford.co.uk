import os
from dotenv import load_dotenv
from pinecone import Pinecone

# Load env variables
load_dotenv() 

# Initialize Pinecone instance
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# List all indexes
existing_indexes = pc.list_indexes()

# Fetch and display index details
index_details = {}
for index_info in existing_indexes:
    index_name = index_info.name
    index_description = pc.describe_index(index_name)
    index_details[index_name] = {
        "dimensions": index_description.dimension,
        "metadata_config": index_description.metadata_config
    }

# Print details of all indexes
for name, details in index_details.items():
    print(f"Index: {name}, Dimensions: {details['dimensions']}, Metadata Config: {details['metadata_config']}")
