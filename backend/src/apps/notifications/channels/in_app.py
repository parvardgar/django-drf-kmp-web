from .base import NotificationChannelStrategy


class InAppChannel(NotificationChannelStrategy):

    def send(
        self,
        recipient,
        message: str,
        subject: str | None = None,
    ):
        print(
            f"IN_APP -> user:{recipient.id}"
        )