import requests

from arduino.interfaces.api import IApi


class APIService(IApi):
    """API service."""
    def __init__(self, login: str, password: str) -> None:
        response = requests.post("http://localhost:8000/api/auth/token/login/",
                                 json={"username": login, "password": password})
        self.headers = {"Authorization": f"Token {response.json().get('auth_token')}"}

    async def ping(self) -> int:
        """This method checks the status of the web server."""
        response = requests.get("http://localhost:8000/api/ping/")
        return response.status_code

    async def get_card(self, card) -> dict:
        """This method gets the card from web-server."""
        url = f"http://localhost:8000/api/cards/{card}/"
        response = requests.get(url, headers=self.headers)
        return response.json()

    async def post_attendance(self, card) -> dict:
        """This method create user attendance by post card id to web-server."""
        url = f"http://localhost:8000/api/attendance/"
        response = requests.post(url, json={"card": card}, headers=self.headers)
        return response.json()
