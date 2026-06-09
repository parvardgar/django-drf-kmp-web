from notifications.enums import (
    NotificationChannel,
    NotificationEvent,
)


NOTIFICATION_TEMPLATES = {
    NotificationEvent.OTP_CREATED: {
        "channels": [
            NotificationChannel.SMS,
            NotificationChannel.EMAIL,
        ],
        "subject": "Verification Code",
        "message": "Your verification code is {otp}",
    },

    NotificationEvent.USER_REGISTERED: {
        "channels": [
            NotificationChannel.EMAIL,
            NotificationChannel.PUSH,
            NotificationChannel.IN_APP,
        ],
        "subject": "Welcome",
        "message": "Welcome {name}",
    },
}