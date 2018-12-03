import pytest
from echovr_api.team import Team

@pytest.fixture
def team(standard_public_match_gamestate):
    return standard_public_match_gamestate.teams[0]

def test_team(team):
    assert team.team == "BLUE TEAM"

def test_possession(team):
    assert team.possession == False

def test_players(team):
    expected_player_names = ["Bob", "Jack", "Jill"]
    assert len(team.players) == len(expected_player_names)

    actual_player_names = [player.name for player in team.players]
    assert sorted(expected_player_names) == sorted(actual_player_names)

def test_stats(team):
    assert team.stats != None
    assert team.stats.points == 6

def test_color(team):
    assert team.color == Team.Color.BLUE

def test_name(team):
    assert team.name == "BLUE TEAM"

def test_score(team):
    assert team.score == 6
