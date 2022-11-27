from flask import Flask

from dotenv import load_dotenv
from logging import basicConfig
from os import environ

load_dotenv(override=True)
basicConfig(filename='basic.log')

app = Flask(__name__)

if environ.get('APP_CONFIG', 'local') == 'local':
    app.config.from_pyfile('config/development.py')
else:
    app.config.from_pyfile('config/production.py')

if __name__ == '__main__':
    app.run(debug=app.config.get('DEBUG', False))