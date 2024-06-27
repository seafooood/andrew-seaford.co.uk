# How To Install PostgreSQL on Unbuntu

## Installation

To install PostgreSQL on Ubuntu, follow these steps:

- Install the PostgreSQL package

    ```bash
    sudo apt install postgresql postgresql-contrib
    ```

- Start the PostgreSQL service

    ```bash
    sudo systemctl start postgresql
    ```

- Enable PostgreSQL to start on boot

    ```bash
    sudo systemctl enable postgresql
    ```

- Switch to the PostgreSQL user

    ```bash
    sudo -i -u postgres
    ```

- Access the PostgreSQL prompt

    ```bash
    psql
    ```

    Once in the PostgreSQL prompt, you can perform various database operations. To exit the prompt, type `\q`.

- In the PostgreSQL prompt, set the password for the postgres user

    ```sql
    ALTER USER postgres PASSWORD 'newpassword';
    ```

## Create Test Database

- Switch to the PostgreSQL user

    ```bash
    sudo -i -u postgres
    ```

- Access the PostgreSQL prompt

    ```bash
    psql
    ```

Once in the PostgreSQL prompt, you can perform various database operations. To exit the prompt, type `\q`.

- Create a new database

    ```bash
    createdb mydatabase
    ```

- Confirm the database has been created using the command `\l` to list databases.

    ![command l](commandl.png)

- Connect to the database `\c mydatabase`

- Create a table

    ```sql
    CREATE TABLE employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        position VARCHAR(50),
        salary NUMERIC
    );
    ```

- Confirm the table was created using the command `\dt`

    ![commanddt](commanddt.png)

- Insert test data

    ```sql
    INSERT INTO employees (name, position, salary) VALUES ('John Doe', 'Manager', 60000);
    INSERT INTO employees (name, position, salary) VALUES ('Jane Smith', 'Developer', 55000);
    ```

- Execute a simple query

    ```sql
    SELECT * FROM employees;
    ```

    ![select](select.png)

## Connect To The Test Database Using Python

- Install the psycopg2 module

    ```bash
    pip install psycopg2-binary
    ```

- Create a python file `nano p.py`

    ```python
    import psycopg2

    # Database connection parameters
    db_params = {
        'dbname': 'mydatabase',
        'user': 'postgres',
        'password': 'yourpassword',
        'host': 'localhost',
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
    ```

- Execute the Python file

    ```bash
    python3 p.py
    ```

    ![python](python.png)


