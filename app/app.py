import re
from datetime import datetime
from typing import Union

import phonenumbers
from flask import Flask, request

from database import collection

PHONE_REGEX = r'^(\+)?[\d\s]+$'
EMAIL_REGEX = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}$'


app = Flask(__name__)


def is_date(value: str) -> bool:
    """Проверяет, является ли строка датой в формате DD.MM.YYYY или YYYY-MM-DD.

    Аргументы:
        value (str): Строка для проверки.

    Возвращает:
        bool: True, если строка является датой, иначе False.
    """

    formats = ['%d.%m.%Y', '%Y-%m-%d']
    for format in formats:
        try:
            datetime.strptime(value, format)
            return True
        except ValueError:
            pass
    return False


def is_phone_number(value: str) -> bool:
    """Проверяет, является ли строка телефонным номером,
    используя модуль phonenumbers.

    Аргументы:
        value (str): Строка для проверки.

    Возвращает:
        bool: True, если строка является допустимым
        телефонным номером, иначе False.
    """

    try:
        phone_number = phonenumbers.parse(str(value))
        if (
            phonenumbers.is_valid_number(phone_number)
            and re.match(PHONE_REGEX, str(value))
        ):
            return True
    except Exception:
        pass
    return False


def is_email(value: str) -> bool:
    """Проверяет, является ли строка email.

    Аргументы:
        value (str): Строка для проверки.

    Возвращает:
        bool: True, если строка является допустимым email, иначе False.
    """

    if re.match(EMAIL_REGEX, value):
        return True
    return False


def validate_request_data(data: dict) -> dict:
    """Определяет типы данных в полях запроса.
    Проверяет на соответствие типам: date, phone, email.
    Всем остальным полям присваивает тип string.

    Аргументы:
        data (dict): Данные запроса.

    Возвращает:
        dict: Валидированные данные с указанием типов полей.
    """

    for key, value in data.items():

        if is_date(value):
            data[key] = 'date'
            continue

        if is_phone_number(value):
            data[key] = 'phone'
            continue

        if is_email(value):
            data[key] = 'email'
            continue

        data[key] = 'string'

    return data


def find_match_forms(validated_data: dict) -> list:
    """Определяет совпадения полей запроса с полями шаблонов форм по их
    названию и типу. Возвращает список с именами совпавших форм.

    Аргументы:
        validated_data (dict): Валидированные данные запроса.

    Возвращает:
        list: Имена совпавших форм.
    """

    match_forms = []
    forms = collection.find({}, {"_id": 0})

    for form in forms:
        if all(
            field_name in validated_data
            and (
                form[field_name] == validated_data[field_name]
                or form[field_name] == 'string'
            )
            for field_name in form.keys()
            if field_name != 'name'  # пропускает имена шаблонов форм
        ):
            match_forms.append(form['name'])
    return sorted(match_forms)


@app.route('/get_form', methods=['POST'])
def get_form() -> Union[list, dict]:
    """Обрабатывает запрос на сравнение формы.

    Возвращает имена совпавших форм, если они есть,
    в противном случае возвращает валидированные данные.

    Возвращает:
        Union[list, dict]: Имена совпавших форм или валидированные данные.
    """

    request_data = dict(request.args)
    validated_data = validate_request_data(request_data)
    match_forms_names = find_match_forms(validated_data)
    if match_forms_names:
        return match_forms_names
    else:
        return validated_data


if __name__ == '__main__':
    app.run(port=8000)
