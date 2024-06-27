import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'mydatabase',
    'user': 'postgres',
    'password': 'newpassword',
    'host': '192.168.127.223',
    'port': '5432'
}

try:
    # Connect to the PostgreSQL database
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Execute the query
    cursor.execute("SELECT * FROM employees;")
    
    # Fetch all the results
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

except (Exception, psycopg2.DatabaseError) as error:
    print(f"Error: {error}")
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
