import os
from dotenv import load_dotenv

# Load the settings from the .env file
load_dotenv()

# Get the value for the setting myName
myName = os.getenv("myName")
print("MyName=", myName)
print("logFilename=", os.getenv("logFilename"))