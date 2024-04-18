import asyncio

import requests
import serial as arduino_listener

from arduino.services.interfaces import IRepository, IApi, IReceiver, IArduinoSerial


class App:
    def __init__(self, receiver: IReceiver):
        self.receiver = receiver

    async def start(self) -> None:
        while True:
            await self.receiver.receive()
            await asyncio.sleep(delay=3)


class APIService(IApi):
    def __init__(self):
        response = requests.post("http://localhost:8000/api/auth/token/login/",
                                 json={"username": "a", "password": "a"})
        self.headers = {"Authorization": f"Token {response.json().get('auth_token')}"}

    async def get(self, card) -> dict:
        url = f"http://localhost:8000/api/cards/{card}/"
        response = requests.get(url, headers=self.headers)
        return response.json()

    async def post(self, card) -> dict:
        url = f"http://localhost:8000/api/attendance/"
        response = requests.post(url, json={"card": card}, headers=self.headers)
        return response.json()


class ArduinoSerial(IArduinoSerial):
    def __init__(self, com: str, port: int):
        self.serial = arduino_listener.Serial(com, port)

    async def send_to_arduino(self, message: str) -> None:
        self.serial.write(message.encode())


class Receiver(IReceiver):
    def __init__(self,
                 arduino: IArduinoSerial,
                 repository: IRepository,
                 api_service: IApi):
        self.arduino = arduino
        self._repository = repository
        self.api_service = api_service

    async def receive(self) -> None:
        decoded_data = self.arduino.serial.readline().decode()
        card_from_web = await self.api_service.get(card=decoded_data)
        is_web_card_blocked = card_from_web.get("is_blocked")

        if not is_web_card_blocked:
            await self.arduino.send_to_arduino("true")
            await self.api_service.post(card=decoded_data)
            card_from_local = await self._repository.find(parameter=decoded_data)

            if card_from_local is None:
                await self._repository.create(data={"card": decoded_data, "is_blocked": is_web_card_blocked})
                return

            if is_web_card_blocked != card_from_local.get("is_blocked"):
                await self._repository.update({"card": decoded_data, "is_blocked": is_web_card_blocked})
                return
        else:
            await self.arduino.send_to_arduino("false")
