from celery import shared_task

from notifications.providers.sms.kavenegar import (
    KavenegarSmsProvider,
)


@shared_task(
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 5},
)
def send_sms_task(
    *,
    mobile: str,
    template: str,
    tokens: list[str],
):
    provider = KavenegarSmsProvider()

    provider.send(
        mobile=mobile,
        template=template,
        tokens=tokens,
    )