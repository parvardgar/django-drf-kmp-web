from abc import ABC, abstractmethod


class NotificationChannelStrategy(ABC):

    @abstractmethod
    def send(
        self,
        *,
        recipient,
        config: dict,
        context: dict,
    ) -> None:
        raise NotImplementedError