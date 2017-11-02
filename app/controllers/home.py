""" This module contains all the view functions for the recipes app"""
from flask import render_template, Blueprint, session, redirect, url_for, request, flash
from app.utilities import register, login




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
        return redirect(url_for('home.sign_in'))


@home_blueprint.route('/register', methods=["GET", "POST"])
def sign_up():
    """ Handles the sign_up route """
    if request.method == 'POST':
        result = register(request.form['name'], request.form['username'], request.form['password']
                          , request.form['rpt_password'])
        if result == "Registration successful":
            flash(result, 'info')
            return redirect(url_for('home.sign_in'))
        flash(result, 'warning')
    return render_template('register.html')


@home_blueprint.route('/login', methods=['GET', 'POST'])
def sign_in():
    """ Handles the sign_in route """
    if request.method == 'POST':
        result = login(request.form['username'], request.form['password'])
        if result == "Login successful":
            session['username'] = request.form['username']
            return redirect(url_for('read_categories'))
        flash(result, 'warning')
    return render_template('login.html')
    
