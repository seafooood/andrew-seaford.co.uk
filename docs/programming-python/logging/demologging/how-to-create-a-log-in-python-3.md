---
title: "How To Create a Log in Python 3"
keywords: [python, logging, debugging, log-files, python3]
---

# How To Create a Log in Python 3

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

### Full script

```python
import logging

# Configure the logging settings
logging.basicConfig(level=logging.DEBUG,  # Set the logging level to DEBUG for all messages
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='example.log')  # Log messages to a file named example.log

def main():
    logging.info("Script started.")
    
    # Your script code here
    
    try:
        result = 10 / 0  # Simulating an error for demonstration
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    # More script code
    
    logging.info("Script finished.")

if __name__ == "__main__":
    main()

```

### Example of the log file created by the script

```log
2023-12-23 18:32:33,383 - INFO - Script started.
2023-12-23 18:32:33,383 - ERROR - An error occurred: division by zero
2023-12-23 18:32:33,383 - INFO - Script finished.
````

## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-python/logging/demologging](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-python/logging/demologging)
