from typing import List
from stats import Stats
from geometry import Vector3D

"""Represents the state of a single player in the current game"""
class Player():
    """
    Initialize the player with data from the API.

    Parameters:

    - `name`
        The username of the player.
    - `playerid`
        A number representing ID of the player within the current game session.
    - `userid`
        A unique number identifying the player across all game sessions.
    - `possession`
        Indicates whether this player currently has posession of the disk.
    - `position`
        The current position of the player within the arena
    - `stats`
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
