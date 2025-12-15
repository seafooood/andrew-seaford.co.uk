# Code based on example from https://docs.pinecone.io/guides/inference/generate-embeddings

# Import the Pinecone library
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec

# Initialize a Pinecone client with your API key
pc = Pinecone(api_key="pcsk_kMWjL_ATJPss75WFZyD29YFsY4odcbQaTDiXT7Fanfyx69Xe9hheXrWFs2SyEgGZHnEmg")

# Define a sample dataset where each item has a unique ID and piece of text
data = [
    {"id": "vec1", "text": "Apple is a popular fruit known for its sweetness and crisp texture."},
    {"id": "vec2", "text": "The tech company Apple is known for its innovative products like the iPhone."},
    {"id": "vec3", "text": "Many people enjoy eating apples as a healthy snack."},
    {"id": "vec4", "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
    {"id": "vec5", "text": "An apple a day keeps the doctor away, as the saying goes."},
    {"id": "vec6", "text": "Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership."}
]

# Convert the text into numerical vectors that Pinecone can index
embeddings = pc.inference.embed(
    model="multilingual-e5-large",
    inputs=[d['text'] for d in data],
    parameters={"input_type": "passage", "truncate": "END"}
)

print(embeddings)

# 4. Upsert embeddings

# Target the index where you'll store the vector embeddings
index = pc.Index("test-index")

# Prepare the records for upsert
# Each contains an 'id', the embedding 'values', and the original text as 'metadata'
records = []
for d, e in zip(data, embeddings):
    records.append({
        "id": d['id'],
        "values": e['values'],
        "metadata": {'text': d['text']}
    })

# Upsert the records into the index
index.upsert(
    vectors=records,
    namespace="example-namespace"
)

