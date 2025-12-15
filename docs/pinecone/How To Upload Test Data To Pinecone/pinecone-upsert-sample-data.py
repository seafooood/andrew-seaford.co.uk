import os
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(
    api_key="pcsk_kMWjL_ATJPss75WFZyD29YFsY4odcbQaTDiXT7Fanfyx69Xe9hheXrWFs2SyEgGZHnEmg"
)

# Now do stuff
index_name = 'test-index'
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric='euclidean',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )

# Connect to the index
index = pc.Index(index_name)

# Sample data to insert (128-dimensional vectors in this example)
data = [
    ("id1", [0.1] * 1536),
    ("id2", [0.2] * 1536),
    ("id3", [0.3] * 1536)
]

# Upsert (insert or update) the vectors into the index
index.upsert(vectors=data)

print("Data imported successfully!")
