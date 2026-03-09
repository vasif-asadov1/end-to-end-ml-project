import sys
from types import ModuleType
import logger
import logging

def error_message_details(error, error_detail: ModuleType):
    _,_,exc_tb = error_detail.exc_info()
    error_message = f"Error occurred in script: {exc_tb.tb_frame.f_code.co_filename} at line number: {exc_tb.tb_lineno} error message: {str(error)}"
    return error_message

class CustomException(Exception): 
    def __init__(self, error_message, error_detail: ModuleType):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message
    

        


    