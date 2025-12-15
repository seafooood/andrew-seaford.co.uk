import openai
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

query_text = "Books about surviving in space with science"

# 1. Generate the vector from the query
embedding_response = openai.embeddings.create(
    model="text-embedding-3-small",
    input=[query_text]
)
query_vector = embedding_response.data[0].embedding

# 2. Query the DB with the vector
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)
cursor = conn.cursor()

cursor.execute(
    """
    SELECT title, author, description_embedding <-> %s::vector AS distance
    FROM books
    ORDER BY distance ASC
    LIMIT 5;
    """,
    (query_vector,)
)

results = cursor.fetchall()
for row in results:
    print(f"Title: {row[0]}, Author: {row[1]}, Distance: {row[2]:.4f}")

cursor.close()
conn.close()
