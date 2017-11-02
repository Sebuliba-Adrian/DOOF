
from flask import Flask
from app.controllers.home import home_blueprint

 
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.cfg')

app.register_blueprint(home_blueprint)


if __name__ == '__main__':
    app.run(debug=True)