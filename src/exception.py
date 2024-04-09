import sys

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    error_file_name = exc_tb.tb_frame.f_code.co_filename
    error_line_no = exc_tb.tb_lineno
    error_message = f"Error occured in python script name [{error_file_name}] line number [{error_line_no}] error message [{str(error)}]"
    return error_message



class CustomeException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super.__init__(error_message)
        self.error_message= error_message_detail(error=error_message, error_detail=error_detail)


    def __str__(self) -> str:
        return self.error_message
    