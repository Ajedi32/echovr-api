import pytest

@pytest.fixture
def disk(standard_public_match_gamestate):
    return standard_public_match_gamestate.disc

def test_disc_position(disk):
    assert disk.position != None
    assert disk.position.x == 0
    assert disk.position.y == 0
    assert disk.position.z == 0

def test_disc_velocity(disk):
    assert disk.velocity != None
    assert disk.velocity.x == 0
    assert disk.velocity.y == 0
    assert disk.velocity.z == 0

def test_disc_bounce_count(disk):
    assert disk.bounce_count == 0
