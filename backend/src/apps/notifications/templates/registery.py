from notifications.enums import (
    NotificationChannel,
    NotificationEvent,
)


NOTIFICATION_TEMPLATES = {
    NotificationEvent.OTP_CREATED: {
        "channels": [
            NotificationChannel.SMS,
        ],
        NotificationChannel.SMS: {
            "template": "otp",
            "tokens": ["otp"],
        },
    }
}