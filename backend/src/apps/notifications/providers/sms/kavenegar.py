import requests

from django.conf import settings

from .base import BaseSmsProvider


class KavenegarSmsProvider(BaseSmsProvider):

    def send(
        self,
        *,
        mobile: str,
        template: str,
        tokens: list[str],
    ) -> None:
        url = (
            f"https://api.kavenegar.com/v1/"
            f"{settings.KAVENEGAR_API_KEY}"
            f"/verify/lookup.json"
        )

        data = {
            "receptor": mobile,
            "template": template,
        }

        for index, value in enumerate(tokens, start=1):
            key = (
                "token"
                if index == 1
                else f"token{index}"
            )

            data[key] = value

        requests.post(
            url=url,
            data=data,
            timeout=10,
        )