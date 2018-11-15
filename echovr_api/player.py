from typing import List
from echovr_api.stats import Stats
from echovr_api.geometry import Vector3D

class Player():
    """Represents the state of a single player in the current game

    :param name:
        The username of the player.
    :param playerid:
        A number representing ID of the player within the current game session.
    :param userid:
        A unique number identifying the player across all game sessions.
    :param possession:
        Indicates whether this player currently has posession of the disk.
    :param position:
        The current position of the player within the arena
    :param stats:
        A dict containing data used to instantiate the player's current stats.
    """
    def __init__(self, name: str = "", playerid: int = None, userid: int = None,
                       possession: bool = False, position: List[float] = None,
                       stats: dict = {}):
        self.name = name
        self.playerid = playerid
        self.userid = userid
        self.possession = possession

        self.position = Vector3D(*position)
        self.stats = Stats(**stats)
