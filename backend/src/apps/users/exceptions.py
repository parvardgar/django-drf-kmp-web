from common.exceptions import ApplicationException


class UserAlreadyExistsException(ApplicationException):
    status_code = 400
    message = "User with this mobile already exists."
    error_code = "USER_ALREADY_EXISTS"


class OTPExpiredException(ApplicationException):
    status_code = 400
    message = "OTP has expired."
    error_code = "OTP_EXPIRED"


class OTPInvalidException(ApplicationException):

    status_code = 400
    message = "Invalid OTP."
    error_code = "OTP_INVALID"