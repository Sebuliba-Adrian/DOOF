from flask import Flask
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')
users_store = {}
app.secret_key = 'secret'

from .import views