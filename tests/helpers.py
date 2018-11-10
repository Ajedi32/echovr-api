from os import path
import json

FIXTURES_DIR = path.join(path.dirname(__file__), fixtures)

def read_json_file(file):
    with open(file, "r") as fp:
        return json.load(fp)

def fixture(name):
    return read_json_file(path.join(FIXTURES_DIR, f"{name}.json"))
