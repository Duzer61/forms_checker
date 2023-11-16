import re
from datetime import datetime

from flask import Flask, request
import phonenumbers

from database import collection

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
    print('тут не дата')
    return False