import re
from datetime import datetime

from flask import Flask, request
import phonenumbers

from database import collection


PHONE_REGEX = r'^(\+)?[\d\s]+$'
EMAIL_REGEX = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}$'


app = Flask(__name__)


def is_date(value):
    """Проверяет, является ли строка датой в формате
    DD.MM.YYYY или YYYY-MM-DD."""

    formats = ['%d.%m.%Y', '%Y-%m-%d']
    for format in formats:
        try:
            datetime.strptime(value, format)
            return True
        except ValueError:
            pass
    return False


def is_phone_number(value):
    """Проверяет, является ли строка телефонным номером.
    используя модуль phonenumbers."""

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


def is_email(value):
    """Проверяет, является ли строка email."""

    if re.match(EMAIL_REGEX, value):
        return True
    return False


def validate_request_data(data):
    """Определяет типы данных в полях запроса.
    Проверяет на соответствие типам: date, phone, email.
    Всем остальным полям присваивает тип string."""

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


def find_match_forms(validated_data):
    """Определяет совпадения полей запроса с полями шаблонов форм по их
    названию и типу. Возвращает список с именами совпавших форм."""

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
