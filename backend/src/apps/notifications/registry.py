from notifications.enums import NotificationChannel

from notifications.channels.sms import SmsChannel
from notifications.channels.email import EmailChannel
from notifications.channels.push import PushChannel
from notifications.channels.in_app import InAppChannel


CHANNEL_REGISTRY = {
    NotificationChannel.SMS: SmsChannel(),
    NotificationChannel.EMAIL: EmailChannel(),
    NotificationChannel.PUSH: PushChannel(),
    NotificationChannel.IN_APP: InAppChannel(),
}