from django.core.cache import cache
from django.db import transaction

from common.cache.keys import CacheKeys
from apps.users.models import User
from apps.users.exceptions import OTPExpiredException, OTPInvalidException

@transaction.atomic
def register_user(
    *,
    mobile: str,
    otp: str,
):
    cached_otp = cache.get(
        CacheKeys.REGISTRATION_OTP.format(
            mobile=mobile
        )
    )

    if cached_otp is None:
        raise OTPExpiredException()

    if cached_otp != otp:
        raise OTPInvalidException()

    user = User.objects.create_user(
        mobile=mobile,
    )

    cache.delete(
        CacheKeys.REGISTRATION_OTP.format(
            mobile=mobile
        )
    )

    return user