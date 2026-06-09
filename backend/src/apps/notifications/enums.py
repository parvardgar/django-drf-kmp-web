from django.db import models


class NotificationEvent(models.TextChoices):
    OTP_CREATED = "otp_created", "OTP Created"
    USER_REGISTERED = "user_registered", "User Registered"


class NotificationChannel(models.TextChoices):
    SMS = "sms", "SMS"
    EMAIL = "email", "Email"
    PUSH = "push", "Push"
    IN_APP = "in_app", "In App"