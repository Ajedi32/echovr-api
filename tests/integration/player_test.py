import pytest

@pytest.fixture
def player(standard_public_match_gamestate):
    return standard_public_match_gamestate.teams[0].players[0]

def test_name(player):
    assert player.name == "Bob"

def test_playerid(player):
    assert player.playerid == 0

def test_userid(player):
    assert player.userid == 4814054792376258

def test_level(player):
    assert player.level == 8

def test_number(player):
    assert player.number == 76

def test_possession(player):
    assert player.possession == False

def test_stunned(player):
    assert player.stunned == False

def test_blocking(player):
    assert player.blocking == False

def test_invulnerable(player):
    assert player.invulnerable == False

def test_position(player):
    assert player.position != None
    assert player.position.x == -10.598001
    assert player.position.y == 3.9720001
    assert player.position.z == 26.736002

def test_velocity(player):
    assert player.velocity != None
    assert player.velocity.x == -2.131
    assert player.velocity.y == -0.63000005
    assert player.velocity.z == 0.33400002

def test_lhand(player):
    assert player.lhand != None
    assert player.lhand.x == -10.419001
    assert player.lhand.y == 3.5290003
    assert player.lhand.z == 26.732

def test_rhand(player):
    assert player.rhand != None
    assert player.rhand.x == -10.416
    assert player.rhand.y == 3.5430002
    assert player.rhand.z == 26.869001

def test_forward(player):
    assert player.forward != None
    assert player.forward.x == 0.57100004
    assert player.forward.y == -0.26800001
    assert player.forward.z == -0.77600002

def test_left(player):
    assert player.left != None
    assert player.left.x == -0.80800003
    assert player.left.y == -0.017000001
    assert player.left.z == -0.58900005

def test_up(player):
    assert player.up != None
    assert player.up.x == 0.14500001
    assert player.up.y == 0.96300006
    assert player.up.z == -0.22600001

def test_stats(player):
    assert player.stats != None
    assert player.stats.possession_time == 12.294746

def test_username(player):
    assert player.username == "Bob"
