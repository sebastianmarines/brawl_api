class API:
    base: str = "https://api.brawlstars.com/v1"
    players: str = "/players"


def format_tag(tag: str) -> str:
    return "%23" + tag.strip("#").upper()