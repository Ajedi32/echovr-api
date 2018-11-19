from typing import List
from echovr_api.geometry import Vector3D

class Disk():
    """Represents the state of the Disk.

    Initialized using data directly from the Echo VR API. See `the Echo VR API
    documentation`__ for further details on the attributes associated with this
    class, and the expected intialization parameters.

    __ https://github.com/Ajedi32/echovr_api_docs#disc

    :param position: The position_ of the Disk within the arena
    :param velocity: The current velocity_ of the Disk
    :param bounce_count: The number of times the disk has bounced

    .. _position:
    .. _velocity: https://github.com/Ajedi32/echovr_api_docs#vectors
    """
    def __init__(self, position: List[float] = [0.0, 0.0, 0.0],
                       velocity: List[float] = [0.0, 0.0, 0.0],
                       bounce_count: int = 0):

        #: A :class:`~.Vector3D` representing the current position of the disk
        self.position = Vector3D(*position)

        #: A :class:`~.Vector3D` representing the current velocity of the disk
        self.velocity = Vector3D(*velocity)

        #: The number of times the disk has bounced
        self.bounce_count = bounce_count
