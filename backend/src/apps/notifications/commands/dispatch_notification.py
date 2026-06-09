from notifications.registry import (
    CHANNEL_REGISTRY,
)

from notifications.templates.registery import (
    NOTIFICATION_TEMPLATES,
)


def dispatch_notification(
    *,
    event,
    recipient,
    context: dict | None = None,
):
    context = context or {}

    template = NOTIFICATION_TEMPLATES[event]

    subject = template.get("subject")

    message = template["message"].format(
        **context
    )

    channels = template["channels"]

    for channel in channels:

        strategy = CHANNEL_REGISTRY[channel]

        strategy.send(
            recipient=recipient,
            message=message,
            subject=subject,
        )