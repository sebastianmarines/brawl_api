from __future__ import annotations

from typing import Any, Dict, Iterator, List, Optional

from pydantic import BaseModel, Field
from datetime import date


class ClubBase(BaseModel):
    tag: Optional[str]
    name: Optional[str]


class Icon(BaseModel):
    id: Optional[int]


class Gadget(BaseModel):
    name: Optional[str]
    id: int


class StarPower(BaseModel):
    name: Optional[str]
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
    tag: Optional[str] = None
    name: Optional[str] = None


class Player(PlayerBase):
    club: Optional[ClubBase] = None
    is_qualified_from_championship_challenge: Optional[bool] = Field(
        None, alias='isQualifiedFromChampionshipChallenge')
    field_3vs3_victories: Optional[int] = Field(None, alias='3vs3Victories')
    icon: Optional[Icon] = None
    trophies: Optional[int] = None
    exp_level: Optional[int] = Field(None, alias='expLevel')
    exp_points: Optional[int] = Field(None, alias='expPoints')
    highest_trophies: Optional[int] = Field(None, alias='highestTrophies')
    power_play_points: Optional[int] = Field(None, alias='powerPlayPoints')
    highest_power_play_points: Optional[int] = Field(
        None, alias='highestPowerPlayPoints')
    solo_victories: Optional[int] = Field(None, alias='soloVictories')
    duo_victories: Optional[int] = Field(None, alias='duoVictories')
    best_robo_rumble_time: Optional[int] = Field(None,
                                                 alias='bestRoboRumbleTime')
    best_time_as_big_brawler: Optional[int] = Field(
        None, alias='bestTimeAsBigBrawler')
    brawlers: Optional[List[Brawler]] = None
    name_color: Optional[str] = Field(None, alias='nameColor')


class Event(BaseModel):
    mode: Optional[str]
    id: int
    map: Optional[str]


class EventPlayer(PlayerBase):
    brawler: BrawlerBase


class BattleResult(BaseModel):
    mode: Optional[str]
    type: Optional[str]
    teams: List[List[EventPlayer]]


class Battle(BaseModel):
    battle: BattleResult
    battle_time: Optional[str] = Field(..., alias='battleTime')
    event: Event


class Battlelog(BaseModel):
    __root__: List[Battle]

    def __iter__(self):
        return iter(self.__root__)

    def __getitem__(self, item) -> Battle:
        return self.__root__[item]


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
