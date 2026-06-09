from .base import NotificationChannelStrategy


class PushChannel(NotificationChannelStrategy):

    def send(
        self,
        recipient,
        message: str,
        subject: str | None = None,
    ):
        print(
            f"PUSH -> user:{recipient.id}"
        )