from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, validator

from brawl_api.utils import format_date


class ClubBase(BaseModel):
    tag: str
    name: str


class Icon(BaseModel):
    id: int


class Gadget(BaseModel):
    name: str
    id: int


class StarPower(BaseModel):
    name: str
    id: int


class BrawlerBase(BaseModel):
    id: int
    name: Optional[str]
    power: int
    trophies: int


class Brawler(BrawlerBase):
    gadgets: List[Gadget]
    star_powers: List[StarPower] = Field(..., alias='starPowers')
    rank: int
    highest_trophies: int = Field(..., alias='highestTrophies')


class PlayerBase(BaseModel):
    tag: str
    name: str


class Player(PlayerBase):
    club: Optional[ClubBase] = Field(None)
    is_qualified_from_championship_challenge: bool = Field(
        alias='isQualifiedFromChampionshipChallenge')
    field_3vs3_victories: int = Field(alias='3vs3Victories')
    icon: Icon
    trophies: int
    exp_level: int = Field(alias='expLevel')
    exp_points: int = Field(alias='expPoints')
    highest_trophies: int = Field(alias='highestTrophies')
    power_play_points: Optional[int] = Field(None, alias='powerPlayPoints')
    highest_power_play_points: Optional[int] = Field(
        None, alias='highestPowerPlayPoints')
    solo_victories: int = Field(alias='soloVictories')
    duo_victories: int = Field(alias='duoVictories')
    best_robo_rumble_time: Optional[int] = Field(None,
                                                 alias='bestRoboRumbleTime')
    best_time_as_big_brawler: Optional[int] = Field(
        None, alias='bestTimeAsBigBrawler')
    brawlers: List[Brawler]
    name_color: Optional[str] = Field(None, alias='nameColor')

    @validator("club", pre=True)
    def ignore_empty_club(cls, v):
        return v if v else None


class Event(BaseModel):
    mode: Optional[str]
    id: int
    map: Optional[str]


class EventPlayer(PlayerBase):
    brawler: BrawlerBase


class BattleResult(BaseModel):
    mode: str
    type: str
    teams: List[List[EventPlayer]]


class Battle(BaseModel):
    battle: BattleResult
    battle_time: datetime = Field(..., alias='battleTime')
    event: Event

    @validator("battle_time", pre=True)
    def format_battle_time(cls, v):
        return format_date(v)


class Battlelog(BaseModel):
    __root__: List[Battle]

    def __iter__(self):
        return iter(self.__root__)

    def __getitem__(self, item) -> Battle:
        return self.__root__[item]

    @validator("__root__", pre=True)
    def get_items(cls, v: dict):
        if (items := v.get("items")):
            return items
        else:
            return []


class ClubMember(PlayerBase):
    trophies: int
    role: str
    name_color: str = Field(..., alias="nameColor")
    icon: Icon


class Club(ClubBase):
    description: str
    trophies: int
    required_trophies: int = Field(..., alias="requiredTrophies")
    club_type: str = Field(..., alias="type")
    badge_id: int = Field(..., alias="badgeId")
    members: List[ClubMember]


class MemberList(BaseModel):
    __root__: List[ClubMember]

    def __iter__(self):
        return iter(self.__root__)

    def __getitem__(self, item) -> ClubMember:
        return self.__root__[item]

    @validator("__root__", pre=True)
    def get_items(cls, v: dict):
        return v.get("items")