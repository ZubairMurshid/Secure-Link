import logging
import sys

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("governance_audit.log"), # Saves to file for later analysis
            logging.StreamHandler(sys.stdout)           # Prints to console
        ]
    )