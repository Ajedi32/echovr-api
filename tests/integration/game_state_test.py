from echovr_api.team import Team

def test_single_player_private_instantiation(single_player_private_gamestate):
    assert single_player_private_gamestate != None

def test_standard_public_match_instantiation(standard_public_match_gamestate):
    assert standard_public_match_gamestate != None

def test_client_name(standard_public_match_gamestate):
    assert standard_public_match_gamestate.client_name == "TestUser"

def test_sessionid(standard_public_match_gamestate):
  assert standard_public_match_gamestate.sessionid == "0C087AF1-C947-462A-8206-C06D64B1910A"

def test_match_type(standard_public_match_gamestate):
    assert standard_public_match_gamestate.match_type == "Echo_Arena_Public"

def test_map_name(standard_public_match_gamestate):
    assert standard_public_match_gamestate.map_name == "mpl_arena_a"

def test_private_match(standard_public_match_gamestate):
    assert standard_public_match_gamestate.private_match == False

def test_tournament_match(standard_public_match_gamestate):
    assert standard_public_match_gamestate.tournament_match == False

def test_game_clock_display(standard_public_match_gamestate):
    assert standard_public_match_gamestate.game_clock_display == "01:04.60"

def test_game_clock(standard_public_match_gamestate):
    assert standard_public_match_gamestate.game_clock == 64.609161

def test_game_status(standard_public_match_gamestate):
    assert standard_public_match_gamestate.game_status == "playing"

def test_possession(standard_public_match_gamestate):
    assert standard_public_match_gamestate.possession == [1, 0]

def test_blue_points(standard_public_match_gamestate):
    assert standard_public_match_gamestate.blue_points == 0

def test_orange_points(standard_public_match_gamestate):
    assert standard_public_match_gamestate.orange_points == 0

def test_disc(standard_public_match_gamestate):
    assert standard_public_match_gamestate.disc != None
    assert standard_public_match_gamestate.disc.bounce_count == 0

def test_last_score(standard_public_match_gamestate):
    assert standard_public_match_gamestate.last_score != None
    assert standard_public_match_gamestate.last_score.disc_speed == 0

def test_teams(standard_public_match_gamestate):
    assert len(standard_public_match_gamestate.teams) == 2
    assert standard_public_match_gamestate.teams[0].team == "BLUE TEAM"
    assert standard_public_match_gamestate.teams[1].team == "ORANGE TEAM"

def test_players(standard_public_match_gamestate):
    expected_player_names = ["Bob", "Jack", "Jill", "Matt", "John", "Mary"]
    assert len(standard_public_match_gamestate.players) == len(expected_player_names)

    actual_player_names = [player.name for player in standard_public_match_gamestate.players]
    assert sorted(expected_player_names) == sorted(actual_player_names)

def test_blue_team(standard_public_match_gamestate):
    assert standard_public_match_gamestate.blue_team.name == "BLUE TEAM"

def test_orange_team(standard_public_match_gamestate):
    assert standard_public_match_gamestate.orange_team.name == "ORANGE TEAM"

def test_find_player_by_username(standard_public_match_gamestate):
    john = standard_public_match_gamestate.find_player(username = "John")
    assert john != None
    assert john.name == "John"

def test_find_team_by_color(standard_public_match_gamestate):
    blue_team = standard_public_match_gamestate.find_team(color = Team.Color.BLUE)
    orange_team = standard_public_match_gamestate.find_team(color = Team.Color.ORANGE)
    assert blue_team != None
    assert blue_team.name == "BLUE TEAM"
    assert orange_team.name == "ORANGE TEAM"
