import pytest
from echovr_api.team import Team

@pytest.fixture
def last_score(standard_public_match_gamestate):
    return standard_public_match_gamestate.last_score

def test_disc_speed(last_score):
    assert last_score.disc_speed == 0.0

def test_team_color(last_score):
    assert last_score.team_color == Team.Color.BLUE

def test_goal_type(last_score):
    assert last_score.goal_type == "[NO GOAL]"

def test_point_amount(last_score):
    assert last_score.point_amount == 0

def test_distance_thrown(last_score):
    assert last_score.distance_thrown == 0.0

def test_person_scored_username(last_score):
    assert last_score.person_scored_username == "[INVALID]"

def test_assist_scored_username(last_score):
    assert last_score.assist_scored_username == "[INVALID]"

def test_team(last_score):
    assert last_score.team != None
    assert last_score.team.name == "BLUE TEAM"

def test_person_scored(last_score):
    assert last_score.person_scored == None

def test_assist_scored(last_score):
    assert last_score.assist_scored == None

def test_game_state(last_score, standard_public_match_gamestate):
    assert last_score.game_state == standard_public_match_gamestate
