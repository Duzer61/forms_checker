from flask import Flask
from views import get_form

app = Flask(__name__)

app.route('/get_form', methods=['POST'])(get_form)

if __name__ == '__main__':
    app.run(port=8000)
