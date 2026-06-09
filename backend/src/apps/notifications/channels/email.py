from .base import NotificationChannelStrategy


class EmailChannel(NotificationChannelStrategy):

    def send(
        self,
        recipient,
        message: str,
        subject: str | None = None,
    ):
        print(
            f"EMAIL -> {recipient.email}"
        )