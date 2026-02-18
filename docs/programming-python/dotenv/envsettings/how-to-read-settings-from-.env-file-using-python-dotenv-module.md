---
keywords: [python, dotenv, environment variables, configuration, .env file]
---

# How To Read Settings From .env File Using Python Dotenv Module

The Dotenv Python module provides an easy way to read settings from a .env file.

- Install the Python module

```sh
pip install python-dotenv
```

- Create a text file called `.env`. In this example, the setting file will contain one setting called "myName" with the value "andrew"

```txt
myName=andrew
```

- Create a Python file. The important parts of the script are
  - Import the module using `from dotenv import load_dotenv`.
  - Load the settings from the `.env` file using `load_dotenv()`
  - Get the value for the setting called myName using `os.getenv("myName")`

```python
import os
from dotenv import load_dotenv

# Load the settings from the .env file
load_dotenv()

# Get the value for the setting myName
myName = os.getenv("myName")
print("MyName=", myName)
```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-python/dotenv/envsettings](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-python/dotenv/envsettings)
