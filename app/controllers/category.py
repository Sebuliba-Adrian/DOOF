# app/controllers/recipe.py
from flask import render_template, Blueprint


categories_blueprint = Blueprint('recipes',
                              __name__,
                              template_folder='../templates/recipe',
                              url_prefix=None)


@categories_blueprint.route('/')
def index():
    return render_template('categories.html')
