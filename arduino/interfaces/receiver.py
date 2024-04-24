from abc import ABC, abstractmethod


class IReceiver(ABC):
    @abstractmethod
    async def receive(self) -> None: ...