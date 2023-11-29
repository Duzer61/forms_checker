import re
from datetime import datetime

import phonenumbers

PHONE_REGEX = r'^(\+)?[\d\s]+$'
EMAIL_REGEX = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}$'


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
        elif is_phone_number(value):
            data[key] = 'phone'
        elif is_email(value):
            data[key] = 'email'
        else:
            data[key] = 'string'
    return data
