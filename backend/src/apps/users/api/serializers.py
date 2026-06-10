from rest_framework import serializers


class RequestRegistrationOtpSerializer(
    serializers.Serializer
):
    mobile = serializers.CharField(
        max_length=11
    )

    
class RegisterSerializer(
    serializers.Serializer
):
    mobile = serializers.CharField(
        max_length=11
    )

    otp = serializers.CharField(
        max_length=6
    )