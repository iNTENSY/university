from abc import ABC, abstractmethod


class IApi(ABC):
    @abstractmethod
    async def ping(self) -> int: ...

    @abstractmethod
    async def get_card(self, *args, **kwargs) -> dict: ...

    @abstractmethod
    async def post_attendance(self, *args, **kwargs) -> None: ...