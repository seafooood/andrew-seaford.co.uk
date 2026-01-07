# Django Database Seeding

Create a fresh database on start Django application and seed it with default data is a common and recommended practice for ensuring a consistent development and testing environment. You can achieve this by creating a script that runs when your Docker container starts, which will handle the database setup and data seeding.

Here is a step-by-step guide on how to configure your Django project and Docker container to achieve this:

### Step 1: Create a Custom Django Management Command to Seed Your Database

You can create a custom management command that reads data from a text file (like a CSV) and populates your database. This allows you to check your seed data into version control.

1.  **Structure your app for management commands:**
    Inside one of your Django apps, create the following directory structure:
    ```
    your_app/
    ├── management/
    │   └── __init__.py
    │   └── commands/
    │       ├── __init__.py
    │       └── seed_data.py
    └── __init__.py
    └── models.py
    ...
    ```

2.  **Create the `seed_data.py` command:**
    This Python script will define the logic for seeding your database. Here's an example of how to read from a CSV file named `seed_data.csv` and populate a `YourModel` model.

    In `your_app/management/commands/seed_data.py`:
    ```python
    import csv
    from django.core.management.base import BaseCommand
    from your_app.models import YourModel # Replace with your actual app and model

    class Command(BaseCommand):
        help = 'Seeds the database with initial data from a CSV file'

        def handle(self, *args, **options):
            # Define the path to your seed data file
            seed_data_file = 'your_app/seed_data.csv'

            # Clear existing data from the model to ensure a fresh start
            YourModel.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Successfully cleared existing data for YourModel.'))

            try:
                with open(seed_data_file, 'r') as file:
                    reader = csv.reader(file)
                    next(reader)  # Skip the header row
                    for row in reader:
                        # Create a new model instance for each row in the CSV
                        YourModel.objects.create(
                            field1=row[0],
                            field2=row[1],
                            # Add other fields as necessary
                        )
                self.stdout.write(self.style.SUCCESS('Successfully seeded the database.'))
            except FileNotFoundError:
                self.stdout.write(self.style.ERROR(f'Seed data file not found at: {seed_data_file}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'An error occurred while seeding the database: {e}'))

    ```

3.  **Create your seed data file:**
    Create a `seed_data.csv` file within your app directory. You can now easily track changes to this file with Git.

    `your_app/seed_data.csv`:
    ```csv
    field1,field2
    value1,value2
    another_value1,another_value2
    ```

### Step 2: Create a Startup Script for Your Docker Container

Create a shell script that will be executed every time your container starts. This script will ensure the database is fresh and then seed it.

1.  **Create a script file:**
    In the root of your project, create a file named `entrypoint.sh`.

    `entrypoint.sh`:
    ```bash
    #!/bin/sh

    # Exit immediately if a command exits with a non-zero status.
    set -e

    # It's a good practice to remove the old database file if it exists
    # to ensure a completely fresh start, especially with SQLite.
    if [ -f "db.sqlite3" ]; then
        echo "Removing old database."
        rm db.sqlite3
    fi

    # Run database migrations
    echo "Running database migrations..."
    python manage.py migrate

    # Seed the database with initial data
    echo "Seeding the database..."
    python manage.py seed_data

    # Start the Django development server
    exec "$@"
    ```

2.  **Make the script executable:**
    Before building your Docker image, make sure this script is executable:
    ```bash
    chmod +x entrypoint.sh
    ```

### Step 3: Configure Your Dockerfile to Use the Startup Script

Modify your `Dockerfile` to copy the `entrypoint.sh` script and set it as the entrypoint.

`Dockerfile`:
```dockerfile
# Start from a Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Copy the entrypoint script and make it executable
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

# The default command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### How It Works

*   When you start your Docker container, the `ENTRYPOINT` in your `Dockerfile` will execute the `entrypoint.sh` script.
*   The script will first delete the old `db.sqlite3` file if it exists.
*   Then, `python manage.py migrate` will create a new, empty database with the correct schema.
*   After that, your custom `python manage.py seed_data` command will run, populating the new database with the data from your `seed_data.csv` file.
*   Finally, the `CMD` from your `Dockerfile` (or `docker-compose.yml`) will be executed, starting your Django application.

This approach gives you a clean, predictable database state every time you start your container, with your seed data managed in a version-controlled text file as you wanted.

## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming%20python/django/Django%20Database%20Seeding](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming%20python/django/Django%20Database%20Seeding)
