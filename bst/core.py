import requests
from requests.sessions import Session

from bst.utils import API, format_tag

from bst.models import Battlelog, Player, Club, MemberList


class Client:
    session: Session

    def __init__(self, token: str) -> None:
        self.session = requests.Session()
        self.headers = {
            'Authorization': f'Bearer {token}',
        }

    def _request(self, route):
        with self.session as session:
            return session.get(API.base + route, headers=self.headers)

    def get_player(self, player_tag) -> Player:
        player_tag = format_tag(player_tag)
        json_resp = self._request(f"{API.players}/{player_tag}").json()
        return Player.parse_obj(json_resp)

    def get_player_battlelog(self, player_tag) -> Battlelog:
        player_tag = format_tag(player_tag)
        json_resp = self._request(
            f"{API.players}/{player_tag}/battlelog").json()
        return Battlelog.parse_obj(json_resp["items"])

    def get_club(self, club_tag) -> Club:
        club_tag = format_tag(club_tag)
        json_resp = self._request(f"{API.club}/{club_tag}").json()
        return Club.parse_obj(json_resp)

    def get_club_members(self, club_tag) -> MemberList:
        club_tag = format_tag(club_tag)
        json_resp = self._request(f"{API.club}/{club_tag}/members").json()
        return MemberList.parse_obj(json_resp["items"])
