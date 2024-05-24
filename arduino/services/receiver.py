from arduino.interfaces.receiver import IReceiver


class Receiver(IReceiver):
    async def receive(self) -> None:
        decoded_data: str = await self.arduino.get_from_arduino()

        if not decoded_data.startswith("CARD UID: "):
            return

        parsed_card_uid = decoded_data.split(": ")[1]  # Example: ["Card UID", "05 09 24 09"]
        card_from_web = await self.api_service.get_card(card=parsed_card_uid)

        if not card_from_web.get("is_blocked"):
            await self.arduino.send_to_arduino("true")
            await self.api_service.post_attendance(card=parsed_card_uid)
        else:
            await self.arduino.send_to_arduino("false")