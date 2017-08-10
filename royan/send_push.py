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
    'custom_content': {
        'model': None,
        'type': None,
        'id': None
    }
}


def send_push(model, type, id):
    data_base['custom_content']['model'] = model
    data_base['custom_content']['type'] = type
    data_base['custom_content']['id'] = id
    requests.post(PUSH_URL,
                  headers=headers,
                  data=json.dumps(data_base))
