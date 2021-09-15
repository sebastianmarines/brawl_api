from pydantic import BaseModel, Field


class Player(BaseModel):
    is_qualified_from_championship_challenge: bool = Field(
        ..., alias="isQualifiedFromChampionshipChallenge")
    victories_3vs3: int = Field(..., alias="3vs3Victories")
    tag: str
    name: str
    trophies: int