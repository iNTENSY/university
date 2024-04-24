import asyncio
from http import HTTPStatus

from arduino.interfaces.app import IApp
from arduino.interfaces.receiver import IReceiver


class App(IApp):
    def __init__(self, receiver: IReceiver):
        self.receiver = receiver

    async def start(self) -> None:
        status_code = await self.receiver.api_service.ping()

        if status_code != HTTPStatus.OK:
            return

        while True:
            await self.receiver.receive()
            await asyncio.sleep(delay=3)
