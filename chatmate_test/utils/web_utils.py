import requests
import json

def get_json_response(data):
    response = requests.Response()
    response._content = json.dumps(data).encode('utf-8')
    return response