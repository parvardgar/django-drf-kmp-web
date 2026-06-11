import secrets

from django.core.cache import cache

from apps.users.models import User
from common.cache.keys import CacheKeys

from apps.notifications.enums import NotificationEvent
from apps.notifications.commands.dispatch_notification import dispatch_notification
from apps.users.exceptions import UserAlreadyExistsException

def request_registration_otp(
    mobile: str,
):
    if User.objects.filter(
        mobile=mobile,
    ).exists():
        raise UserAlreadyExistsException()
    
    otp = "".join(
        secrets.choice("0123456789")
        for _ in range(6)
    )

    cache.set(
        CacheKeys.REGISTRATION_OTP.format(
            mobile=mobile
        ),
        otp,
        timeout=120,
    )
    class Recipient:
        mobile = None

    recipient = Recipient()
    recipient.mobile = mobile

    dispatch_notification(
        event=NotificationEvent.OTP_CREATED,
        recipient=recipient,
        context={
            "otp": otp,
        },
    )