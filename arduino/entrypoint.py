import asyncio

from arduino.repository.repository import Repository
from arduino.services.application import ArduinoSerial, APIService, Receiver, App


if __name__ == '__main__':
    arduino = ArduinoSerial(com="COM6", port=9200)
    api = APIService()
    repository = Repository()
    receiver = Receiver(arduino, repository, api)
    app = App(receiver)
    asyncio.run(app.start())
