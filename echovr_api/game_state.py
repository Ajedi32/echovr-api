from typing import List
from echovr_api.team import Team
from echovr_api.disk import Disk
from echovr_api.last_score import ContextualizedLastScore
import logging

class InvalidGameStateError(Exception):
    """Thrown when the state data passed to GameState is invalid"""
    pass

class GameState():
    """Represents the current state of a game sesion.

    Initialized using data directly from the Echo VR API. See `the Echo VR API
    documentation`__ for further details on the attributes associated with this
    class, and the expected intialization parameters.

    __ https://github.com/Ajedi32/echovr_api_docs#properties

    :param client_name:
        The username of the currently signed-in user.
    :param sessionid:
        A 128-bit string-encoded GUID.
    :param match_type:
        Represents the type of match being played.
    :param map_name:
        Represents the current "map" (environment) the user is playing in.
    :param private_match:
        Whether the current session is a private match.
    :param tournament_match:
        Whether the current session is being used for an official tournament.
    :param game_clock_display:
        A human-readable representation of the current game clock time.
    :param game_clock:
        The current game clock time, in seconds.
    :param game_status:
        The current game's status.
    :param possession:
        An arry of two integers representing which team currently posesses the
        disk.
    :param blue_points:
        The current score of the blue team.
    :param orange_points:
        The current score of the orange team.
    :param disc:
        A dict representing the current state of the disk.
    :param last_score:
        A dict containing facts and statistics related to the last goal scored.
    :param teams:
        An array of dicts containing data used to instantiate the game's two
        teams.

    :raises InvalidGameStateError:
        Raised when you attempt to initialize the game into a state that doesn't
        make sense (such as having three teams).
    """
    def __init__(self, client_name: str = None, sessionid: str = None,
                       match_type: str = "INVALID GAMETYPE",
                       map_name: str = "INVALID LEVEL",
                       private_match: bool = False,
                       tournament_match: bool = False,
                       game_clock_display: str = None,
                       game_clock: float = None, game_status: str = 'unknown',
                       possession: List[int] = [], blue_points: int = 0,
                       orange_points: int = 0, disc: dict = {},
                       last_score: dict = {}, teams: List[dict] = []):

        #: The username of the currently signed-in user.
        self.client_name = client_name

        #: A 128-bit string-encoded GUID.
        self.sessionid = sessionid

        #: Represents the type of match being played.
        self.match_type = match_type

        #: Represents the current "map" (environment) the user is playing in.
        self.map_name = map_name

        #: Whether the current session is a private match.
        self.private_match = private_match

        #: Whether the current session is being used for an official tournament.
        self.tournament_match = tournament_match

        #: A human-readable representation of the current game clock time.
        self.game_clock_display = game_clock_display

        #: The current game clock time, in seconds.
        self.game_clock = game_clock

        #: The current game's status.
        self.game_status = game_status

        #: An arry of two integers representing which team currently posesses
        #: the disk.
        self.possession = possession

        #: The current score of the blue team.
        self.blue_points = blue_points

        #: The current score of the orange team.
        self.orange_points = orange_points

        #: A :class:`~.Disk` object representing the current state of the disk.
        self.disc = Disk(**disc)

        #: A :class:`~.ContextualizedLastScore` object containing facts and
        #: statistics related to the last goal scored.
        self.last_score = ContextualizedLastScore(self, **last_score)

        if len(teams) != 2:
            raise InvalidGameStateError("Unexpected number of teams: %s" % len(teams))

        #: An array of both :class:`~.Team`\ s currently in the game
        self.teams = [Team(**data) for data in teams]

        #: An array of all :class:`~.Player`\ s currently in the game
        self.players = [player for team in self.teams for player in team.players]

        # Note: The positions of the blue and orange teams in the array seem to
        # be fixed. Judging color by team name is unreliable, since players can
        # set a custom team name for themselves by pressing F11.

        #: The :class:`~.Team` object representing the blue team
        self.blue_team = self.teams[0]
        self.blue_team.color = Team.Color.BLUE

        #: The :class:`~.Team` object representing the orange team
        self.orange_team = self.teams[1]
        self.orange_team.color = Team.Color.ORANGE

        # Just in case I'm wrong (or a team decides to be a smart aleck), log
        # it...
        if self.blue_team == 'ORANGE TEAM' or self.orange_team == 'BLUE TEAM':
            logging.warn("Blue/Orange teams might be backwards (judging by their names).")

    def find_player(self, username: str = None):
        """Find the :class:`~.Player` with the given properties

        Returns the player whose attributes match the given properties, or
        ``None`` if no match is found.

        :param username: The username of the Player
        """
        if username != None:
            return next((player for player in self.players if player.name == username), None)
        else:
            return None

    def find_team(self, color: str = None):
        """Find the :class:`~.Team` with the given properties

        Returns the team whose attributes match the given properties, or
        ``None`` if no match is found.

        :param color: The :class:`~.Team.Color` of the Team
        """
        if color != None:
            if color is Team.Color.BLUE:
                return self.blue_team
            else:
                return self.orange_team
        else:
            return None
