
# Проект "Forms_checker". Написан в качестве тестового задания для [LeadHit](https://leadhit.ru/)

### Описание задания доступно [по ссылке](https://docs.google.com/document/d/1fMFwPBs53xzcrltEFOpEG4GWTaQ-5jvVLrNT6_hmC7I/edit#heading=h.pieurecv5l1j)
Я немного расширил задание и добавил возможность делать запросы не только вида "**f_name1=value1&f_name2=value2**", но и через аргументы в запросе и через json.
___
### Для запуска проекта в контейнерах на локальной машине должен быть установлен [Docker](https://www.docker.com/).

Краткая инструкция по запуску:
- скачать проект на локальную машину `git clone git@github.com:Duzer61/forms_checker.git`
- в терминале перейти в директорию с проектом:  `cd <путь к проекту>/forms_checker`
- для запуска проекта в контейнерах в директории  `/forms_checker` выполнить команду `docker compose stop && docker compose up --build`
- дождаться сборки и запуска контейнеров с проектом
- БД будет автоматически заполнена тестовыми данными из файла /app/initial_data.py
- **POST** запросы можно направлять на url: http://127.0.0.1:8000/get_form
- Примеры запросов (удобно использовать Postman): 
	- `http://127.0.0.1:8000/get_form?sender=me&recipient=they&message=Hi%20there&datestamp=16.11.2023`
	- `http://127.0.0.1:8000/get_form?username=JohnDoe&phone=%2B79055555555`
	- `http://127.0.0.1:8000/get_form?sender=me&date=16.11.2023&date_fake=30.02.2023&phone=%2B79055555555&phone_fake=%2B790555555559&email=example@mail.com&email_fake=example@@mail.com`
	- `username=Peter&phone=+79055555555`
	- 	``
	{"username": "Гвидо ван Россум", "email": "email@mail.ru", "password": "anypass"}
	``
___

В проекте реализован скрипт для демонстрации работы. Файл `demo.py` находится в

директории `forms_checker/demo/`

Для запуска демонстрации необходимо развернуть виртуальное окружение:
- в терминале перейти в директорию `forms_checker/demo/`
- создать виртуальное окружение командой `python3 -m venv venv` (команда для Linux. Для Windows или macOS может отличаться. В проекте применялся python3.12)
- активировать виртуальное окружение  `source venv/bin/activate` (для Windows `source venv/Scripts/activate`)
- установить зависимости. При активированном виртуальном окружении выполнить команду: `pip install -r requirements.txt`
- после установки зависимостей можно запускать демо. Для этого в терминале, находясь в той же директории `forms_checker/demo/` при активированном виртуальном окружении запустить файл `demo.py` команда: `python3 demo.py`
- В терминале будут выведены примеры запросов и ответы на них

## Технологии в проекте:
 - Python 3.12
 - Docker
 - Nginx
 - Gunicorn
 - MongoDB
 - Flask
 
 ## Автор
Данил Кочетов - [GitHub](https://github.com/Duzer61)