from typing import Union

from flask import request

from checker import find_match_forms
from utils import handle_post_request
from validators import validate_request_data


def get_form() -> Union[list, dict]:
    """Обрабатывает запрос на сравнение формы.

    Возвращает имена совпавших форм, если они есть,
    в противном случае возвращает валидированные данные.

    Возвращает:
        Union[list, dict]: Имена совпавших форм или валидированные данные.
    """

    request_data = handle_post_request(request)
    validated_data = validate_request_data(request_data)
    match_forms_names = find_match_forms(validated_data)
    if match_forms_names:
        return match_forms_names
    else:
        return validated_data
