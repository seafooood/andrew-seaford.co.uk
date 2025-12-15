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
