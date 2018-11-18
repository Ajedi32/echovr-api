from echovr_api.team import Team

class LastScore():
    """Statistics about the most recent goal scored in the current game.

    Initialized using data directly from the Echo VR API. See `the Echo VR API
    documentation`__ for further details on the attributes associated with this
    class, and the expected intialization parameters.

    __ https://github.com/Ajedi32/echovr_api_docs#last_score

    :param disc_speed: The speed of the disk when it entered the goal
    :param team: "blue" or "orange" depending on which team scored
    :param goal_type: A human-readable explanation of the type of goal scored
    :param point_amount: The number of points scored (2 or 3)
    :param distance_thrown: The distance the goal was scored from
    :param person_scored: Username of the player who scored the goal
    :param assist_scored: Username of the player who assisted the goal, if any
    """

    def __init__(self, disc_speed: float = 0.0, team: str = "blue",
                       goal_type: str = "[NO GOAL]", point_amount: int = 0,
                       distance_thrown: float = 0.0,
                       person_scored: str = "[INVALID]",
                       assist_scored: str = "[INVALID]"):

        #: The speed of the disk when it entered the goal, in meters/second
        self.disc_speed = disc_speed

        #: The :class:`~.Team.Color` of the team that scored
        self.team_color = Team.Color.by_name(team)

        #: A human-readable explanation of the type of goal scored
        self.goal_type = goal_type

        #: The number of points scored (2 or 3)
        self.point_amount = point_amount

        #: The distance the goal was scored from
        self.distance_thrown = distance_thrown

        #: The username of the player who scored the goal
        self.person_scored_username = person_scored

        #: The username of the player who assisted the goal, if any
        self.assist_scored_username = assist_scored
