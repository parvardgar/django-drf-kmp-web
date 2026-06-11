from apps.notifications.registry import (
    CHANNEL_REGISTRY,
)

from apps.notifications.templates.registery import (
    NOTIFICATION_TEMPLATES,
)


def dispatch_notification(
    *,
    event,
    recipient,
    context: dict | None = None,
):
    context = context or {}

    notification_template = NOTIFICATION_TEMPLATES[event]

    channels = notification_template["channels"]

    for channel in channels:

        strategy = CHANNEL_REGISTRY[channel]

        strategy.send(
            recipient=recipient,
            config=notification_template[channel],
            context=context,
        )