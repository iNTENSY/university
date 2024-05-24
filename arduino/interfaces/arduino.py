from abc import abstractmethod, ABC


class IArduinoSerial(ABC):
    @abstractmethod
    def __init__(self, com: str, port: int):
        self.serial = None

    @abstractmethod
    async def send_to_arduino(self, message: str) -> None: ...

    @abstractmethod
    async def get_from_arduino(self) -> str: ...
