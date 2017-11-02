""" This module contains all the view functions for the recipes app"""
from flask import render_template, Blueprint, session, redirect, url_for, request, flash
from app.utilities import register, login
from app import USERS

home_blueprint = Blueprint(
    'home',
    __name__,
    template_folder="../templates/home"
)


@home_blueprint.route('/')
def index():
    """Handle the index route"""
    if session.get('username'):
        return redirect(url_for('read_categories'))
    else:
        return redirect(url_for('sign_in'))


@home_blueprint.route('/register', methods=["GET", "POST"])
def sign_up():
    """ Handles the registeration route """
    return render_template('index.html')


@home_blueprint.route('/login', methods=['GET', 'POST'])
def sign_in():
    """ Handles the sign_in route """
    if request.method == 'POST':
        result = login(request.form['username'], request.form['password'])
        if result == "Login successful":
            session['username'] = request.form['username']
            return redirect(url_for('read_buckets'))
        flash(result, 'warning')
    return render_template('login.html')
    
