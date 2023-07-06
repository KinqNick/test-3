```python
import logging

def handle_error(error):
    logging.error(f"An error occurred: {error}")

def validate_data(data):
    if not data:
        handle_error("ERROR_INVALID_DATA")
        return False
    return True

def log_message(message):
    logging.info(message)
```