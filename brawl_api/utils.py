from datetime import datetime


class API:
    base = "https://api.brawlstars.com/v1"
    players = "/players"
    club = "/clubs"


def format_tag(tag: str) -> str:
    return "%23" + tag.strip("#").upper()


def format_date(timestamp: str) -> datetime:
    return datetime.strptime(timestamp, '%Y%m%dT%H%M%S.%fZ')