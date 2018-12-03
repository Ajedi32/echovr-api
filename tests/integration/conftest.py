import pytest
from echovr_api.game_state import GameState

@pytest.fixture
def single_player_private_gamestate(single_player_private_data):
    return GameState(**single_player_private_data)

@pytest.fixture
def standard_public_match_gamestate(standard_public_match_data):
    return GameState(**standard_public_match_data)
