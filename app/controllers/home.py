from flask import render_template, Blueprint

home_blueprint = Blueprint(
    'home',
    __name__,
    template_folder="../templates/home"
)


@home_blueprint.route('/')
def index():
    return render_template("index.html")

@home_blueprint.route('/register')
def register():
    return render_template('index.html')

@home_blueprint.route('/login')
def login():
    return render_template('index.html')

