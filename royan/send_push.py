import requests
import json

from royan.settings import PUSH_URL, PUSH_TOKEN, PACKAGE_NAME

headers = {
    'Authorization': 'Token {}'.format(PUSH_TOKEN),
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

data_base = {
    'applications': [PACKAGE_NAME],
    'notification': {
        'show_app': False
    },
    'change': {
        'model': None,
        'type': None,
        'id': None
    }
}


def send_push(model, type, id):
    data_base['change']['model'] = model
    data_base['change']['type'] = type
    data_base['change']['id'] = id
    requests.post(PUSH_URL,
                  headers=headers,
                  data=json.dumps(data_base))
