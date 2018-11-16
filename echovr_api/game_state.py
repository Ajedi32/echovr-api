from typing import List
from echovr_api.team import Team
import logging

class InvalidGameStateError(Exception):
    """Thrown when the state data passed to GameState is invalid"""
    pass

class GameState():
    """Represents the current state of a game sesion.

    :param sessionid:
        A 128-bit string-encoded GUID.
    :param game_clock_display:
        A human-readable representation of the current game clock time.
    :param game_clock:
        The current game clock time, in seconds.
    :param game_status:
        The current game's status.
        Possible values: 'playing', 'post_match', ...?
    :param possession:
        An arry of two integers representing which team currently posesses the
        disk. TODO: Unclear exactly how this data is encoded.
    :param teams:
        An array of dicts containing data used to instantiate the game's two
        teams.

    :raises InvalidGameStateError:
        Raised when you attempt to initialize the game into a state that doesn't
        make sense (such as having three teams).
    """
    def __init__(self, sessionid: str = None, game_clock_display: str = None,
                       game_clock: float = None, game_status: str = 'unknown',
                       possession: List[int] = [], teams: List[dict] = []):
        self.sessionid = sessionid
        self.game_clock_display = game_clock_display
        self.game_clock = game_clock
        self.game_status = game_status
        self.possession = possession

        if len(teams) != 2:
            raise InvalidGameStateError("Unexpected number of teams: %s" % len(teams))

        self.teams = [Team(**data) for data in teams]

        # Position in the array seems stable. Going by team name is unreliable,
        # since players can set a custom team name for themselves by pressing
        # F11.
        self.blue_team = self.teams[0]
        self.blue_team.color = Team.Color.BLUE
        self.orange_team = self.teams[1]
        self.orange_team.color = Team.Color.ORANGE

        # Just in case I'm wrong (or a team decides to be a smart aleck), log
        # it...
        if self.blue_team == 'ORANGE TEAM' or self.orange_team == 'BLUE TEAM':
            logging.warn("Blue/Orange teams might be backwards (judging by their names).")
