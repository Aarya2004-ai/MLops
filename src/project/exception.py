import sys 
import logging
def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()   
    # to store the errror message
    file_name=exc_tb.tb_frame.f_code.co_filename
    return f"Error in {file_name}, line {exc_tb.tb_lineno}: {error}"

class CustomException(Exception):
    def __init__(self, error, error_detail):
        super().__init__(error)
        self.error_message = error_message_details(error, error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        print("INSIDE EXCEPT")   # sanity check
        try:
            raise CustomException(e, sys)
        except CustomException as ce:
            print("OUTPUT:", ce)