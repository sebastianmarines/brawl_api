class API:
    base = "https://api.brawlstars.com/v1"
    players = "/players"
    club = "/clubs"


def format_tag(tag: str) -> str:
    return "%23" + tag.strip("#").upper()