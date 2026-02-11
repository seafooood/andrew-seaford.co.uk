import os
import openai
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "5432")

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)
cursor = conn.cursor()

# Fetch books without embeddings
cursor.execute("SELECT id, description FROM books WHERE description_embedding IS NULL;")
books = cursor.fetchall()

for book_id, description in books:
    try:
        # ✅ New API call
        response = openai.embeddings.create(
            model="text-embedding-3-small",  # or text-embedding-ada-002
            input=[description]  # note: input must be a list
        )
        embedding = response.data[0].embedding  # new structure

        # Update the book record
        cursor.execute(
            "UPDATE books SET description_embedding = %s WHERE id = %s;",
            (embedding, book_id)
        )
        print(f"✅ Updated book ID {book_id}")
    except Exception as e:
        print(f"❌ Failed to update book ID {book_id}: {e}")

conn.commit()
cursor.close()
conn.close()
