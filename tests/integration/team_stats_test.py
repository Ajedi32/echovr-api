import pytest

@pytest.fixture
def team_stats(standard_public_match_gamestate):
    return standard_public_match_gamestate.teams[0].stats

def test_possession_time(team_stats):
    assert team_stats.possession_time == 77.446526

def test_points(team_stats):
    assert team_stats.points == 6

def test_assists(team_stats):
    assert team_stats.assists == 0

def test_saves(team_stats):
    assert team_stats.saves == 0

def test_stuns(team_stats):
    assert team_stats.stuns == 17

def test_goals(team_stats):
    assert team_stats.goals == 0

def test_passes(team_stats):
    assert team_stats.passes == 0

def test_catches(team_stats):
    assert team_stats.catches == 0

def test_steals(team_stats):
    assert team_stats.steals == 0

def test_blocks(team_stats):
    assert team_stats.blocks == 0

def test_interceptions(team_stats):
    assert team_stats.interceptions == 0

def test_shots_taken(team_stats):
    assert team_stats.shots_taken == 4
