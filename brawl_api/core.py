from typing import Generic, Type, TypeVar
from aiohttp.client_reqrep import ClientResponse
from pydantic.main import BaseModel
import requests
import aiohttp
from requests.sessions import Session
from requests import Response

from brawl_api.utils import API, format_tag

from brawl_api.models import Battlelog, Player, Club, MemberList

T = TypeVar('T', Player, Club, Battlelog, MemberList)
R = TypeVar('R', Response, ClientResponse)


class ClientBase:
    def _check_request_error(self, request: R) -> R:
        # TODO
        return request


class Client(ClientBase):
    """Client class
    """
    session: Session

    def __init__(self, token: str) -> None:
        self.session = requests.Session()
        self.headers = {
            'Authorization': f'Bearer {token}',
        }

    def _request(self, route: str) -> dict:
        with self.session as session:
            response = session.get(API.base + route, headers=self.headers)
            response = self._check_request_error(response)
            return response.json()

    def _get_x(self, model: Type[T], url: str) -> T:
        resp = self._request(url)
        return model.parse_obj(resp)

    def get_player(self, player_tag) -> Player:
        """Get player

        Args:
            player_tag (str): Brawl stars player tag

        Returns:
            Player: A Player object
        """
        player_tag = format_tag(player_tag)
        return self._get_x(Player, f"{API.players}/{player_tag}")
        # json_resp = self._request(f"{API.players}/{player_tag}")
        # return Player.parse_obj(json_resp)

    def get_player_battlelog(self, player_tag: str) -> Battlelog:
        """Get player's battlelog

        Args:
            player_tag (str): Brawl stars player tag

        Returns:
            Battlelog: A Battlelog object
        """
        player_tag = format_tag(player_tag)
        return self._get_x(Battlelog, f"{API.players}/{player_tag}/battlelog")
        # json_resp = self._request(f"{API.players}/{player_tag}/battlelog")
        # return Battlelog.parse_obj(json_resp["items"])

    def get_club(self, club_tag: str) -> Club:
        """Get club information

        Args:
            club_tag (str): Brawl Stars club tag

        Returns:
            Club: A Club object
        """
        club_tag = format_tag(club_tag)
        return self._get_x(Club, f"{API.club}/{club_tag}")
        # json_resp = self._request(f"{API.club}/{club_tag}")
        # return Club.parse_obj(json_resp)

    def get_club_members(self, club_tag: str) -> MemberList:
        """Get club members

        Args:
            club_tag (str): Brawl Stars club tag

        Returns:
            MemberList: A MemberList object
        """
        club_tag = format_tag(club_tag)
        return self._get_x(MemberList, f"{API.club}/{club_tag}/members")
        # json_resp = self._request(f"{API.club}/{club_tag}/members")
        # return MemberList.parse_obj(json_resp["items"])


class AsyncClient(ClientBase):
    session: aiohttp.ClientSession

    def __init__(self, token: str) -> None:
        self.session = aiohttp.ClientSession()
        self.headers = {
            'Authorization': f'Bearer {token}',
        }

    async def _request(self, route: str):
        async with self.session.get(API.base + route,
                                    headers=self.headers) as response:
            response = self._check_request_error(response)
            return await response.json()

    async def _get_x(self, model: Type[T], url: str) -> T:
        resp = await self._request(url)
        return model.parse_obj(resp)

    async def get_player(self, player_tag: str) -> Player:
        """Get player

        Args:
            player_tag (str): Brawl stars player tag

        Returns:
            Player: A Player object
        """
        player_tag = format_tag(player_tag)
        return await self._get_x(Player, f"{API.players}/{player_tag}")
        # json_resp = await self._request(f"{API.players}/{player_tag}")
        # return Player.parse_obj(json_resp)

    async def get_player_battlelog(self, player_tag: str) -> Battlelog:
        """Get player's battlelog

        Args:
            player_tag (str): Brawl stars player tag

        Returns:
            Battlelog: A Battlelog object
        """
        player_tag = format_tag(player_tag)
        return await self._get_x(Battlelog,
                                 f"{API.players}/{player_tag}/battlelog")
        # json_resp = await self._request(f"{API.players}/{player_tag}/battlelog"
        #                                 )
        # return Battlelog.parse_obj(json_resp["items"])

    async def get_club(self, club_tag: str) -> Club:
        """Get club information

        Args:
            club_tag (str): Brawl Stars club tag

        Returns:
            Club: A Club object
        """
        club_tag = format_tag(club_tag)
        return await self._get_x(Club, f"{API.club}/{club_tag}")
        # json_resp = await self._request(f"{API.club}/{club_tag}")
        # return Club.parse_obj(json_resp)

    async def get_club_members(self, club_tag: str) -> MemberList:
        """Get club members

        Args:
            club_tag (str): Brawl Stars club tag

        Returns:
            MemberList: A MemberList object
        """
        club_tag = format_tag(club_tag)
        return await self._get_x(MemberList, f"{API.club}/{club_tag}/members")
        # json_resp = await self._request(f"{API.club}/{club_tag}/members")
        # return MemberList.parse_obj(json_resp["items"])