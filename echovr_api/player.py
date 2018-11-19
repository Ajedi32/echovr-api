from typing import List
from echovr_api.stats import Stats
from echovr_api.geometry import Vector3D

class Player():
    """Represents the state of a single player in the current game

    Initialized using data directly from the Echo VR API. See `the Echo VR API
    documentation`__ for further details on the attributes associated with this
    class, and the expected intialization parameters.

    __ https://github.com/Ajedi32/echovr_api_docs#teamsplayers

    :param name:
        The username of the player.
    :param playerid:
        A number representing ID of the player within the current game session.
    :param userid:
        A unique number identifying the player across all game sessions.
    :param level:
        A number (1-50) representing the player's experience "level".
    :param number:
        The number a player chose for themselves in the customization room.
    :param possession:
        Indicates whether this player currently has posession of the disk.
    :param stunned:
        Whether the player is currently stunned.
    :param blocking:
        Whether the player is currently blocking.
    :param invulnerable:
        Whether or not the player is currently immune to stuns.
    :param position:
        The current `position`_ of the player within the arena
    :param velocity:
        The current `velocity`_ (speed and direction of movement) of the player.
    :param lhand:
        The `position`_ of the player's left hand within the Arena.
    :param rhand:
        The `position`_ of the player's right hand within the Arena.
    :param forward:
        The `direction`_ that the player's head is facing.
    :param left:
        The `direction`_ that the left side of the player's head is facing.
    :param up:
        The `direction`_ that the top side of the player's head is facing.
    :param stats:
        A dict containing data used to instantiate the player's current stats.

    .. _position:
    .. _direction:
    .. _velocity: https://github.com/Ajedi32/echovr_api_docs#vectors
    """
    def __init__(self, name: str = "", playerid: int = None, userid: int = None,
                       level: int = 0, number: int = 0,
                       possession: bool = False, stunned: bool = False,
                       blocking: bool = False, invulnerable: bool = False,
                       position: List[float] = None,
                       velocity: List[float] = None, lhand: List[float] = None,
                       rhand: List[float] = None, forward: List[float] = None,
                       left: List[float] = None, up: List[float] = None,
                       stats: dict = {}):

        #: The username of the player.
        self.name = name

        #: A integer representing ID of the player within the current game
        #: session.
        self.playerid = playerid

        #: A unique integer identifying the player across all game sessions.
        self.userid = userid

        #: A integer (1-50) representing the player's experience "level".
        self.level = level

        #: The number a player chose for themselves in the customization room.
        self.number = number

        #: Whether this player currently has posession of the disk.
        self.possession = possession

        #: Whether the player is currently stunned.
        self.stunned = stunned

        #: Whether the player is currently blocking.
        self.blocking = blocking

        #: Whether or not the player is currently immune to stuns.
        self.invulnerable = invulnerable

        #: A :class:`~.Vector3D` represnting the position of the player's head
        self.position = Vector3D(*position)

        #: A :class:`~.Vector3D` representing the current speed and direction of
        #: movement of the player.
        self.velocity = Vector3D(*velocity)

        #: A :class:`~.Vector3D` represnting the position of the player's left
        #: hand
        self.lhand = Vector3D(*lhand)

        #: A :class:`~.Vector3D` represnting the position of the player's right
        #: hand
        self.rhand = Vector3D(*rhand)

        #: A :class:`~.Vector3D` represnting the direction that the player's
        #: head is facing.
        self.forward = Vector3D(*forward)

        #: A :class:`~.Vector3D` represnting the direction that the left side of
        #: the player's head is facing.
        self.left = Vector3D(*left)

        #: A :class:`~.Vector3D` represnting the direction that the top of the
        #: player's head is facing.
        self.up = Vector3D(*up)

        #: The :class:`~.Stats` object for this player
        self.stats = Stats(**stats)

    @property
    def username(self):
        """The username of the player."""
        return self.name
