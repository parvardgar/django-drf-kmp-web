from apps.notifications.enums import NotificationChannel

from apps.notifications.channels.sms import SmsChannel
from apps.notifications.channels.email import EmailChannel
from apps.notifications.channels.push import PushChannel
from apps.notifications.channels.in_app import InAppChannel


CHANNEL_REGISTRY = {
    NotificationChannel.SMS: SmsChannel(),
    NotificationChannel.EMAIL: EmailChannel(),
    NotificationChannel.PUSH: PushChannel(),
    NotificationChannel.IN_APP: InAppChannel(),
}