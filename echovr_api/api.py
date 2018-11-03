import requests
import json
from echovr_api.game_state import GameState

class API(object):
    """Instantiate an API interface for the given base_url."""
    def __init__(self, base_url="http://127.0.0.1/"):
        self.base_url = base_url

    @property
    def _gamestate_url(self):
        return self.base_url.rstrip('/') + "/session"

    """
    Return the raw JSON data from the state/session API.

    Throws:

    - `requests.exceptions.ConnectionError`
        This exception will be thrown if the API is unavaible. This might
        indicate that the user is not currently in a match, or that they didn't
        launch Echo VR with the `-http` option.

    - `json.decoder.JSONDecodeError`
        This exception will be thrown if the data returned by the API is not
        valid JSON. Likely indicates a bug in Echo VR or in this library.
    """
    def fetch_state_data(self):
        response = requests.get(self._gamestate_url)
        response_text = response.text.rstrip('\0')
        return json.loads(response_text)

    """
    Return a GameState object representing the state of the current game session
    as presented by the API.

    Throws:

    - `requests.exceptions.ConnectionError`
        This exception will be thrown if the API is unavaible. This might
        indicate that the user is not currently in a match, or that they didn't
        launch Echo VR with the `-http` option.

    - `json.decoder.JSONDecodeError`
        This exception will be thrown if the data returned by the API is not
        valid JSON. Likely indicates a bug in Echo VR or in this library.
    """
    def fetch_state(self):
        return GameState(**self.fetch_state_data())

"""An instance of API, with the default base URL."""
DEFAULT_API = API()

"""Shortcut for calling fetch_state_data on DEFAULT_API"""
fetch_state_data = DEFAULT_API.fetch_state_data

"""Shortcut for calling fetch_state on DEFAULT_API"""
fetch_state = DEFAULT_API.fetch_state
