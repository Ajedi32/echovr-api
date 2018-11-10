from typing import List
from enum import Enum
from echovr_api.stats import Stats
from echovr_api.player import Player

"""Represents the state of a single team in the current game"""
class Team():
    """Represents the color (blue or orange) of a team"""
    class Color(Enum):
        BLUE = 0
        ORANGE = 1

    """
    Initialize the team with data from the API.

    Parameters:

    - `team`
        A human-readable team name. Usually either "ORANGE TEAM" or "BLUE TEAM",
        but that's subject to change, and may be different during LAN
        tournaments (though I've not yet confirmed this).
    - `possession`
        Indicates whether this team currently has posession of the disk.
    - `players`
        An array of dicts containing data used to instantiate the team's
        players.
    - `stats`
        A dict containing data used to instantiate the team's current stats.
    - `color`
        An enumerable Color representing the color of the team.
    """
    def __init__(self, team: str = "", possession: bool = False,
                       players: List[dict] = [], stats: dict = {},
                       color: Color = None):
        self.team = team
        self.possession = possession

        self.players = [Player(**player_data) for player_data in players]
        self.stats = Stats(**stats)
        self.color = color

    """Better-named alias for team."""
    @property
    def name(self):
        return self.team

    """
    The current score of the team.

    Note: There's currently a bug in the API which makes this inaccurate if the
    team has scored self-goals, but it's the best we have for now. If the API
    ever exposes more accurate data, this method will be updated to take
    advantage of that.
    """
    @property
    def score(self):
        return self.stats.points
