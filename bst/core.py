import requests
from requests.sessions import Session

from bst.utils import API


class Client:
    session: Session

    def __init__(self, token: str) -> None:
        self.session = requests.Session()
        self.headers = {
            'Authorization': f'Bearer {token}',
        }

    def _request(self, url):
        with self.session as session:
            return session.get(url, headers=self.headers)

    def get_player(self, player_tag):
        return self._request(f"{API.base}{API.players}/{player_tag}").json()