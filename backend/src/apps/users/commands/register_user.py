from django.core.cache import cache

from common.cache.keys import CacheKeys
from users.models import User
from users.exceptions import OTPExpiredException, OTPInvalidException

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