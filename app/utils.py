from flask import Request


def handle_post_request(request: Request) -> dict:
    """Извлекает данные из POST-запроса."""

    if (
        request.headers.get('Content-Type') ==
        'application/x-www-form-urlencoded'
    ):
        # Обработка данных в формате application/x-www-form-urlencoded
        request_data = request.form.to_dict()

    elif request.headers.get('Content-Type') == 'application/json':
        # Обработка данных в формате JSON
        request_data = request.get_json()

    elif request.args:
        # Обработка данных в формате URL
        request_data = dict(request.args)

    else:
        request_data = {}

    return request_data
