import json
import os
import time

import requests
from data_demo import req_data

REQ_URL = 'http://127.0.0.1:8000/get_form'


def get_responses():
    """Отправляет POST-запросы и выводит в терминал ответы."""

    for data in req_data:
        try:
            response = requests.post(REQ_URL, data=data, timeout=1)
        except Exception:
            print(f"Error: {data}")
            continue
        response_data = response.text
        print(f'Request: {data}')
        print()
        print('Response:')
        print(
            f'{json.dumps(json.loads(response_data), indent=4)}', end='\n' * 3
        )
        time.sleep(0.7)


def main():
    os.system('clear')
    print('Starting requests...', end='\n' * 3)
    time.sleep(1)
    get_responses()


if __name__ == '__main__':
    main()
