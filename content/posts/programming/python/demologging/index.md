+++
title = 'Demologging'
date = 2024-06-01T21:59:04+01:00
draft = false
+++

## How To Create a Log in Python 3

In this article, we will add logging to a simple Python script.

- Import the logging library `import logging`
- Configure the logging settings

```python
logging.basicConfig(level=logging.DEBUG,  # Set the logging level to DEBUG for all messages
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='example.log')  # Log messages to a file named example.log
```

- Create an infomation log `logging.info("Script started.")`
- Create an error log `logging.error(f"An error occurred: {e}")`

Full script
[DemoLogging.py](DemoLogging.py)

Example of the log file created by the script.
[example.log](example.log)
