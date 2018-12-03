import pytest

@pytest.fixture
def player_stats(standard_public_match_gamestate):
    return standard_public_match_gamestate.teams[0].players[0].stats

def test_possession_time(player_stats):
    assert player_stats.possession_time == 12.294746

def test_points(player_stats):
    assert player_stats.points == 3

def test_assists(player_stats):
    assert player_stats.assists == 0

def test_saves(player_stats):
    assert player_stats.saves == 0

def test_stuns(player_stats):
    assert player_stats.stuns == 6

def test_goals(player_stats):
    assert player_stats.goals == 0

def test_passes(player_stats):
    assert player_stats.passes == 0

def test_catches(player_stats):
    assert player_stats.catches == 0

def test_steals(player_stats):
    assert player_stats.steals == 0

def test_blocks(player_stats):
    assert player_stats.blocks == 0

def test_interceptions(player_stats):
    assert player_stats.interceptions == 0

def test_shots_taken(player_stats):
    assert player_stats.shots_taken == 1
