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
