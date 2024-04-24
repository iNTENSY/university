from abc import ABC, abstractmethod

from arduino.interfaces.api import IApi
from arduino.interfaces.arduino import IArduinoSerial


class IReceiver(ABC):
    def __init__(self, arduino: IArduinoSerial, api_service: IApi) -> None:
        self.arduino = arduino
        self.api_service = api_service

    @abstractmethod
    async def receive(self) -> None: ...