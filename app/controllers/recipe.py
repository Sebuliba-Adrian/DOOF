# app/controllers/recipe.py
from flask import render_template, Blueprint


recipes_blueprint = Blueprint('recipes',
                              __name__,
                              template_folder='../templates/recipe',
                              url_prefix="recipe")


@recipes_blueprint.route('/')
def index():
    return render_template('recipe.html')
