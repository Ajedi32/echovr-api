from typing import List
from enum import Enum
from echovr_api.stats import Stats
from echovr_api.player import Player

class Team():
    """Represents the state of a single team in the current game

    :param team:
        A human-readable team name. Usually either "ORANGE TEAM" or "BLUE TEAM",
        but that's subject to change, and may be different during LAN
        tournaments (though I've not yet confirmed this).
    :param possession:
        Indicates whether this team currently has posession of the disk.
    :param players:
        An array of dicts containing data used to instantiate the team's
        players.
    :param stats:
        A dict containing data used to instantiate the team's current stats.
    :param color:
        An enumerable `Color` representing the color of the team.
    """

    class Color(Enum):
        """Represents the color (blue or orange) of a team"""
        BLUE = 0
        ORANGE = 1

        @classmethod
        def by_name(cls, name):
            """Return the `Color` that matches a given color name"""
            try:
                return cls[name.upper()]
            except ValueError:
                return None

    def __init__(self, team: str = "", possession: bool = False,
                       players: List[dict] = [], stats: dict = {},
                       color: Color = None):
        self.team = team
        self.possession = possession

        self.players = [Player(**player_data) for player_data in players]
        self.stats = Stats(**stats)
        self.color = color

    @property
    def name(self):
        """Better-named alias for `team`."""
        return self.team

    @property
    def score(self):
        """The current score of the team.

        Note: There's currently a bug in the API which makes this inaccurate if
        the team has scored self-goals, but it's the best we have for now. If
        the API ever exposes more accurate data, this method will be updated to
        take advantage of that.
        """
        # Note: game_status.(blue|orange)_score are currently bugged to always
        # return 0. Once that bug is fixed, this should be updated to use those
        # values instead.
        return self.stats.points
