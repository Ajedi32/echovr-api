import requests
import json

if __name__ == "__main__":
    try:
        response = requests.get('http://127.0.0.1/session')
    except requests.exceptions.ConnectionError as e:
        print({'error': "Connection refused. Make sure you're running Echo VR with the -http option and that you're in a match."})

    response_text = response.text.rstrip('\0')

    try:
        response_object = json.loads(response_text)
        print(response_object)
    except json.decoder.JSONDecodeError as e:
        print({'error': "Could not decode response. (Not valid JSON.)"})
