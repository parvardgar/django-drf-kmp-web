from abc import ABC, abstractmethod


class NotificationChannelStrategy(ABC):

    @abstractmethod
    def send(
        self,
        recipient,
        message: str,
        subject: str | None = None,
    ) -> None:
        raise NotImplementedError