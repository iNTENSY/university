from abc import ABC, abstractmethod


class IApi(ABC):
    @abstractmethod
    async def get(self, *args, **kwargs) -> dict: ...

    @abstractmethod
    async def post(self, *args, **kwargs) -> None: ...


class IRepository(ABC):
    @abstractmethod
    async def find(self, *args, **kwargs) -> dict: ...

    @abstractmethod
    async def create(self, *args, **kwargs): ...

    @abstractmethod
    async def update(self, data): ...


class IArduinoSerial(ABC):
    @abstractmethod
    def __init__(self, com: str, port: int):
        self.serial = None

    @abstractmethod
    async def send_to_arduino(self, message: str) -> None: ...


class IReceiver(ABC):
    @abstractmethod
    async def receive(self) -> None: ...
