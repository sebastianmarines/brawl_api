import requests
from requests.sessions import Session

from brawl_api.utils import API, format_tag

from brawl_api.models import Battlelog, Player, Club, MemberList


class Client:
    """Client class
    """
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
        """Get player

        Args:
            player_tag (str): Brawl stars player tag

        Returns:
            Player: A Player object
        """
        player_tag = format_tag(player_tag)
        json_resp = self._request(f"{API.players}/{player_tag}").json()
        return Player.parse_obj(json_resp)

    def get_player_battlelog(self, player_tag) -> Battlelog:
        """Get player's battlelog

        Args:
            player_tag (str): Brawl stars player tag

        Returns:
            Battlelog: A Battlelog object
        """
        player_tag = format_tag(player_tag)
        json_resp = self._request(
            f"{API.players}/{player_tag}/battlelog").json()
        return Battlelog.parse_obj(json_resp["items"])

    def get_club(self, club_tag) -> Club:
        """Get club information

        Args:
            club_tag (str): Brawl Stars club tag

        Returns:
            Club: A Club object
        """
        club_tag = format_tag(club_tag)
        json_resp = self._request(f"{API.club}/{club_tag}").json()
        return Club.parse_obj(json_resp)

    def get_club_members(self, club_tag) -> MemberList:
        """Get club members

        Args:
            club_tag (str): Brawl Stars club tag

        Returns:
            MemberList: A MemberList object
        """
        club_tag = format_tag(club_tag)
        json_resp = self._request(f"{API.club}/{club_tag}/members").json()
        return MemberList.parse_obj(json_resp["items"])
