import api
from requests.exceptions import ConnectionError
import json

def _output_json(data):
    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    api = api.API()
    try:
        response_object = api.fetch_state_data()
    except ConnectionError as e:
        _output_json({'error': "Connection refused. Make sure you're running Echo VR with the -http option and that you're in a match."})
    except json.decoder.JSONDecodeError as e:
        _output_json({'error': "Could not decode response. (Not valid JSON.)"})

    _output_json(response_object)
