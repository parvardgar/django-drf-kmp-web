from .base import NotificationChannelStrategy


class SmsChannel(NotificationChannelStrategy):

    def send(
        self,
        recipient,
        message: str,
        subject: str | None = None,
    ):
        print(
            f"SMS -> {recipient.mobile}: {message}"
        )