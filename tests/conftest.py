from os import path, sep
import json
import pytest

DATA_DIR = path.join(path.dirname(__file__), 'data')

def read_json_file(file):
    with open(file, "r") as fp:
        return json.load(fp)

def json_data(name):
    name = name.replace('/', sep)
    return read_json_file(path.join(DATA_DIR, f"{name}.json"))

@pytest.fixture(scope="module")
def single_player_private_data():
    return json_data('single_player_private')

@pytest.fixture(scope="module")
def standard_public_match_data():
    return json_data('standard_public_match')
