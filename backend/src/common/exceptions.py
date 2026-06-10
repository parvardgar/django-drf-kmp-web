class ApplicationException(Exception):

    status_code = 400
    message = "Application error"
    error_code = "APPLICATION_ERROR"

    def __init__(self, message=None):
        if message:
            self.message = message