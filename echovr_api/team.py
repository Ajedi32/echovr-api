from typing import List
from stats import Stats
from player import Player

"""Represents the state of a single team in the current game"""
class Team():
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
    """
    def __init__(self, team: str = "", possession: bool = False,
                       players: List[dict] = [], stats: dict = {}):
        self.team = team
        self.possession = possession

        self.players = [Player(**player_data) for player_data in players]
        self.stats = Stats(**stats)

    """Better-named alias for team."""
    @property
    def name(self):
        return self.team
