import asyncio

from arduino.interfaces.app import IApp
from arduino.interfaces.receiver import IReceiver


class App(IApp):
    def __init__(self, receiver: IReceiver):
        self.receiver = receiver

    async def start(self) -> None:
        while True:
            await self.receiver.receive()
            await asyncio.sleep(delay=3)
