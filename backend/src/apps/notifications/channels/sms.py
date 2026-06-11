from apps.notifications.tasks import (
    send_sms_task,
)

from .base import (
    NotificationChannelStrategy,
)


class SmsChannel(NotificationChannelStrategy):

    def send(
        self,
        *,
        recipient,
        config: dict,
        context: dict,
    ) -> None:

        tokens = [
            str(context[token_name])
            for token_name in config["tokens"]
        ]
        send_sms_task.delay(
            mobile=recipient.mobile,
            template=config["template"],
            tokens=tokens,
        )