from rest_framework.views import exception_handler

from common.exceptions import ApplicationException


def custom_exception_handler(exc, context):

    if isinstance(exc, ApplicationException):
        from rest_framework.response import Response

        return Response(
            {
                "success": False,
                "message": exc.message,
                "data": None,
                "errors": None,
                "error_code": exc.error_code,
            },
            status=exc.status_code,
        )

    response = exception_handler(exc, context)

    if response is None:
        return None

    return Response(
        {
            "success": False,
            "message": "Request failed",
            "data": None,
            "errors": response.data,
            "error_code": "REQUEST_ERROR",
        },
        status=response.status_code,
    )