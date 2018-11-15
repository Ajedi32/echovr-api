class Stats():
    """Statistics about a player or team within the current game

    :param possession_time:
        Time in seconds that the subject posessed the disk.
    :param points:
        Points scored by the subject.
    :param assists:
        Number of goals assisted by the subject.
    :param saves:
        Number of opposing team goals prevented by the subject.
    :param stuns:
        Number of times the subject has stunned the opposing team.
    :param goals:
        Number of goals scored by the subject.
        TODO: API always returns zero for teams?
    :param passes:
        Number of times the subject successfully completed a pass
        TODO: API always returns zero for teams?
    :param catches:
        Number of times the subject succssfully caught a pass by a team member
    :param steals:
        Number of times the subject stole the disk from the opposing team
    :param blocks:
        Number of times the subject blocked a punch
        TODO: API always returns zero for teams?
    :param interceptions:
        Number of times the subject intercepted a pass by the opposing team
        TODO: API always returns zero for teams?
    :param shots_taken:
        Number of times the subject attempted a shot on goal
    """
    def __init__(self, possession_time: float = 0.0, points: int = 0,
                       assists: int = 0, saves: int = 0, stuns: int = 0,
                       goals: int = 0, passes: int = 0, catches: int = 0,
                       steals: int = 0, blocks: int = 0, interceptions: int = 0,
                       shots_taken: int = 0):
        self.possession_time = possession_time
        self.points = points
        self.assists = assists
        self.saves = saves
        self.stuns = stuns
        self.goals = goals
        self.passes = passes
        self.catches = catches
        self.steals = steals
        self.blocks = blocks
        self.interceptions = interceptions
        self.shots_taken = shots_taken
