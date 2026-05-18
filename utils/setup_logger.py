# Import Python's built-in logging module
#
# Logging is used to record execution details while test runs
#
# Example:
# Test started
# Product selected
# Add to cart clicked
# Test failed
#
# Helps in debugging and defect analysis
import logging


# Import os module
#
# Used for operating system tasks
#
# Example:
# checking folders
# creating directories
# handling file paths
import os



# Function to create and configure logger
#
# Why function?
# So logger setup can be reused anywhere
#
# Example:
# logger = setup_logger()
def setup_logger():


    # Store folder name where logs will be saved
    #
    # Example:
    # project_folder/logs
    log_folder = "logs"



    # Check whether logs folder already exists
    #
    # os.path.exists() returns:
    # True  -> folder exists
    # False -> folder doesn't exist
    if not os.path.exists(log_folder):

        # Create logs folder if missing
        #
        # os.makedirs() creates directory automatically
        os.makedirs(log_folder)



    # Create logger object
    #
    # logging.getLogger("myntra_logger")
    # creates named logger
    #
    # Name helps identify source of logs
    logger = logging.getLogger("myntra_logger")



    # Set logging level
    #
    # INFO means:
    # all INFO messages and above will be recorded
    #
    # Logging levels:
    #
    # DEBUG    -> very detailed info
    # INFO     -> normal execution info
    # WARNING  -> warning messages
    # ERROR    -> errors
    # CRITICAL -> severe failure
    logger.setLevel(logging.INFO)



    # Prevent duplicate log handlers
    #
    # Why?
    # If logger setup runs multiple times,
    # same messages could be written repeatedly
    #
    # logger.handlers stores existing handlers
    #
    # If empty → create handler
    if not logger.handlers:



        # Create file handler
        #
        # FileHandler writes logs into file
        #
        # File:
        # logs/execution.log
        #
        # Example output:
        # 2025-05-18 10:30:11 - INFO - Opening homepage
        file_handler = logging.FileHandler("logs/execution.log")



        # Define log message format
        #
        # %(asctime)s  -> timestamp
        # %(levelname)s -> INFO / ERROR
        # %(message)s  -> actual message
        #
        # Example:
        # 2025-05-18 11:22:10 - INFO - Product added to cart
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )



        # Attach format to file handler
        #
        # So all log messages follow same structure
        file_handler.setFormatter(formatter)



        # Connect file handler to logger
        #
        # Without this:
        # logger creates messages but doesn't save them
        logger.addHandler(file_handler)



    # Return configured logger object
    #
    # Example:
    # logger = setup_logger()
    #
    # Then:
    # logger.info("Opening homepage")
    return logger