# Use the official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements file to the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY app.py /app/

# Expose the application's port
EXPOSE 5500

# Define the command to run the application
CMD ["python", "app.py"]
