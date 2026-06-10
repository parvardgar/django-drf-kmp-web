from abc import ABC, abstractmethod


class BaseSmsProvider(ABC):

    @abstractmethod
    def send(
        self,
        *,
        mobile: str,
        template: str,
        tokens: list[str],
    ) -> None:
        pass