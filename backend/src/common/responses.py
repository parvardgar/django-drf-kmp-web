from rest_framework.response import Response


def success_response(
    data=None,
    message="Success",
    status_code=200,
):
    return Response(
        {
            "success": True,
            "message": message,
            "data": data,
            "errors": None,
            "error_code": None,
        },
        status=status_code,
    )


def error_response(
    message="Error",
    status_code=400,
    errors=None,
    error_code=None,
):
    return Response(
        {
            "success": False,
            "message": message,
            "data": None,
            "errors": errors,
            "error_code": error_code,
        },
        status=status_code,
    )