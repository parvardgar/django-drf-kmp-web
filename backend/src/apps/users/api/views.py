from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.api.serializers import (
    RequestRegistrationOtpSerializer, RegisterSerializer
)
from users.commands.request_registration_otp import request_registration_otp
from users.commands.register_user import register_user
from common.responses import success_response, error_response


class RequestRegistrationOtpView(
    APIView
):
    def post(self, request):
        serializer = (
            RequestRegistrationOtpSerializer(
                data=request.data
            )
        )
        serializer.is_valid(
            raise_exception=True
        )
        request_registration_otp(
            mobile=serializer.validated_data[
                "mobile"
            ]
        )
        return success_response(
            message="Otp Code Sent Successfully."
        )
    

class RegisterView(
    APIView
):

    def post(self, request):
        serializer = RegisterSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        user = register_user(
            mobile=serializer.validated_data[
                "mobile"
            ],
            otp=serializer.validated_data[
                "otp"
            ],
        )

        return success_response(
            message="User created successfully",
            data={
                "id": user.id,
                "mobile": user.mobile,
            },
            status=status.HTTP_201_CREATED,
        )