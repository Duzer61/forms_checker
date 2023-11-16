import time

from pymongo import MongoClient

from initial_data import forms_data


client = MongoClient('mongodb://db:27017/')

db = client['mongo_db']

collection = db['form_templates']


def load_initial_data():
    time.sleep(1)
    for form in forms_data:
        if not collection.find_one({'name': form['name']}):
            collection.insert_one(form)


if __name__ == '__main__':
    load_initial_data()
