import serial as arduino_listener

from arduino.interfaces.arduino import IArduinoSerial


class ArduinoSerial(IArduinoSerial):
    def __init__(self, com: str, port: int):
        self.serial = arduino_listener.Serial(com, port)

    async def send_to_arduino(self, message: str) -> None:
        """This method send message to arduino port."""
        self.serial.write(message.encode())

    async def get_from_arduino(self) -> str:
        """This method read bytes from arduino and returning decoded message."""
        return self.serial.readline().decode()
