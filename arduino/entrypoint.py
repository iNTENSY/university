import asyncio

from arduino.services.api import APIService
from arduino.services.app import App
from arduino.services.arduino import ArduinoSerial
from arduino.services.receiver import Receiver


if __name__ == '__main__':
    arduino = ArduinoSerial(com="COM6", port=9200)
    api = APIService(login="a", password="a")
    receiver = Receiver(arduino, api)
    app = App(receiver)
    asyncio.run(app.start())
