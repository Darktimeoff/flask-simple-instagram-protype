from flask import Flask, render_template

from dotenv import load_dotenv
from logging import basicConfig
from os import environ

from app.posts.views import posts_blueprint

load_dotenv(override=True)
basicConfig(filename='basic.log')

app = Flask(__name__)

app.register_blueprint(posts_blueprint)

def error_404(e):
    return render_template('404.html')

app.register_error_handler(404, error_404)

if environ.get('APP_CONFIG', 'local') == 'local':
    app.config.from_pyfile('config/development.py')
else:
    app.config.from_pyfile('config/production.py')

if __name__ == '__main__':
    app.run(debug=app.config.get('DEBUG', False))