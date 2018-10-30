import api
from requests.exceptions import ConnectionError
from json.decoder import JSONDecodeError

if __name__ == "__main__":
    api = api.API()
    try:
        response_object = api.fetch_state_data()
    except ConnectionError as e:
        print({'error': "Connection refused. Make sure you're running Echo VR with the -http option and that you're in a match."})
    except JSONDecodeError as e:
        print({'error': "Could not decode response. (Not valid JSON.)"})

    print(response_object)
