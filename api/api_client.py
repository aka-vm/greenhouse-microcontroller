try:
    import requests
except:
    import urequests as requests

import json

def request(url, data=None, method='GET', headers=None):
    if data is not None:
        data = json.dumps(data)
    if headers is None:
        headers = {'Content-Type': 'application/json'}
    response = requests.request(method, url, data=data, headers=headers)
    return response.json()