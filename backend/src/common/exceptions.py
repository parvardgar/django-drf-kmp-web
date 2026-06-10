class ApplicationException(Exception):

    status_code = 400
    message = "Application error"
    error_code = "APPLICATION_ERROR"

    def __init__(self, message=None):
        if message:
            self.message = message



class OTPExpiredException(ApplicationException):

    status_code = 400
    message = "OTP has expired."
    error_code = "OTP_EXPIRED"
class OTPInvalidException(ApplicationException):

    status_code = 400
    message = "Invalid OTP."
    error_code = "OTP_INVALID"