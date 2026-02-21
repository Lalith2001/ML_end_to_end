import sys
import logging

def error_msg_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_line_no = exc_tb.tb_lineno
    error_text = "Error occurred in the python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,error_line_no,str(error)
    )
    
    return error_text
    
   # we are inheriting the exception class w.r.t error msg
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_msg_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
        
        
'''
if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("division by zero")
        raise CustomException(e,sys)
    
'''