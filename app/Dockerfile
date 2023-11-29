FROM python:3.12-slim

RUN pip3 install --upgrade pip

WORKDIR /app

RUN pip install gunicorn==20.1.0

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD python db_init.py && gunicorn app:app -b 0.0.0.0:8000