from typing import List
from echovr_api.team import Team

"""Thrown when the state data passed to GameState is invalid"""
class InvalidGameStateError(Exception):
    pass

"""Represents the current state of a game sesion."""
class GameState():
    """
    Initialize the game state with data from the API.

    Parameters:

    - `sessionid`
        A 128-bit string-encoded GUID.
    - `game_clock_display`
        A human-readable representation of the current game clock time.
    - `game_clock`
        The current game clock time, in seconds.
    - `game_status`
        The current game's status.
        Possible values: 'playing', 'post_match', ...?
    - `possession`
        An arry of two integers representing which team currently posesses the
        disk. TODO: Unclear exactly how this data is encoded.
    - `teams`
        An array of dicts containing data used to instantiate the game's two
        teams.
    """
    def __init__(self, sessionid: str = None, game_clock_display: str = None,
                       game_clock: float = None, game_status: str = 'unknown',
                       possession: List[int] = [], teams: List[dict] = []):
        self.sessionid = sessionid
        self.game_clock_display = game_clock_display
        self.game_clock = game_clock
        self.game_status = game_status
        self.possession = possession

        self.teams = [Team(**data) for data in teams]
