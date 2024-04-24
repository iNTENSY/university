from abc import ABC, abstractmethod


class IApp(ABC):
    @abstractmethod
    async def start(self) -> None: ...
