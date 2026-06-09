from django.core.cache import cache

from common.cache.keys import CacheKeys


def get_cached_user(user_id):
    return cache.get(
        CacheKeys.USER.format(id=user_id)
    )


def set_cached_user(user):
    cache.set(
        CacheKeys.USER.format(id=user.id),
        user,
        timeout=300,
    )


def invalidate_user(user_id):
    cache.delete(
        CacheKeys.USER.format(id=user_id)
    )