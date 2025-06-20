import sys
from src.logger import get_logger

# Get the logger instance
logging = get_logger()

def error_message_detail(error, error_detail: sys):
    """Generates detailed error messages."""
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{error}]"
    return error_message

class CustomException(Exception):
    """Custom exception class for handling detailed errors."""
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
