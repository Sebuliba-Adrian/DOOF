""" This module contains all the view functions for the categorylist app"""
import re
from functools import wraps
from . import app
from flask import render_template, session, flash, redirect, url_for, request
from application.models import User
from utilities import register, login
from . import users_store



@app.route('/')
def index():
    """ Handles the index route """
    if session.get('username'):
        return redirect(url_for('read_categories'))
    else:
        return redirect(url_for('sign_in'))

@app.route('/sign_in', methods=['GET','POST'])
def sign_in():
    """ Handles the sign_in route """
    if request.method == 'POST':
        result = login(request.form['username'], request.form['password'])
        if result == "Login successful":
            session['username'] = request.form['username']
            return redirect(url_for('read_categories'))
        flash(result, 'warning')
    return render_template('login.html')

@app.route('/sign_up', methods=['GET','POST'])
def sign_up():
    """ Handles the sign_up route """
    if request.method == 'POST':
        result = register(request.form['name'], request.form['username'], request.form['password']
                          , request.form['rpt_password'])
        if result == "Registration successful":
            flash(result, 'info')
            return redirect(url_for('sign_in'))
        flash(result, 'warning')
    return render_template('register.html')

def login_required(func):
    """ Decorator function to ensure some routes are only accessed by logged in users """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        """ Modified descriprition of the decorated function """
        if not session.get('username'):
            flash('Login to continue', 'warning')
            return redirect(url_for('sign_in', next=request.url))
        return func(*args, **kwargs)
    return decorated_function

@app.route('/read_categories', methods=['GET', 'POST'])
@login_required
def read_categories():
    """ Handles displaying categories """
    return render_template('categories/read.html', categories=users_store[session['username']].categories)

@app.route('/create_category', methods=['GET', 'POST'])
@login_required
def create_category():
    """ Handles new category creation requests """
    if request.method == 'POST':
        result = users_store[session['username']].add_category(request.form['title'])
        if result == 'Category added':
            flash(result, 'info')
        else:
            flash(result, 'warning')
        return redirect(url_for('read_categories'))
    return render_template('categories/create.html')

@app.route('/update_category/<title>', methods=['GET', 'POST'])
@login_required
def update_category(title):
    """ Handles request to update a category """
    session['category_title'] = title
    if request.method == 'POST':
        result = users_store[session['username']].update_category(session['category_title'],
                                                          request.form['title'])
        if result == 'Category updated':
            flash(result, 'info')
        else:
            flash(result, 'warning')
        return redirect(url_for('read_categories'))
    return render_template('categories/update.html')

@app.route('/delete_category/<title>',methods=['GET', 'POST'])
@login_required
def delete_category(title):
    """ Handles request to delete a category """
    result = users_store[session['username']].delete_category(title)
    if result == 'Category deleted':
        flash(result, 'info')
    else:
        flash(result, 'warning')
    return redirect(url_for('read_categories'))

@app.route('/read_recipes/<category_title>', methods=['GET', 'POST'])
@login_required
def read_recipes(category_title):
    """ Handles displaying recipes """
    session['active_category_title'] = category_title
    return render_template('recipes/read.html', recipes=users_store[session['username']]
                           .categories[category_title].recipes)

@app.route('/create_recipe',methods=['GET', 'POST'])
@login_required
def create_recipe():
    """ Handles new recipe creation requests """
    if request.method == 'POST':
        result = users_store[session['username']].categories[session['active_category_title']].add_recipe(
            request.form['description'])
        if result == 'Recipe added':
            flash(result, 'info')
        else:
            flash(result, 'warning')
        return redirect(url_for('read_recipes', category_title=session['active_category_title']))
    return render_template('recipes/create.html', recipes=users_store[session['username']]
                           .categories[session['active_category_title']].recipes)

@app.route('/update_recipe/<description>',methods=['GET', 'POST'])
@login_required
def update_recipe(description):
    """ Handles request to update an recipe """
    session['description'] = description
    if request.method == 'POST':
        des_result = (users_store[session['username']].categories[session['active_category_title']].
                      update_description(session['description'], request.form['description']))
        status_result = (users_store[session['username']].categories[session['active_category_title']].
                         update_status(session['description'], request.form['status']))
        if des_result == 'Recipe updated' or status_result == 'Recipe updated':
            flash('Recipe updated', 'info')
        else:
            flash(des_result, 'warning')
        return redirect(url_for('read_recipes', category_title=session['active_category_title']))
    return render_template('recipes/update.html', recipe=users_store[session['username']]
                           .categories[session['active_category_title']].recipes[description],
                           recipes=users_store[session['username']].
                           categories[session['active_category_title']].recipes)

@app.route('/delete_recipe/<description>',methods=['GET', 'POST'])
@login_required
def delete_recipe(description):
    """ Handles request to delete an recipe """
    result = users_store[session['username']].categories[session['active_category_title']].delete_recipe(
        description)
    if result == 'Recipe deleted':
        flash(result, 'info')
    else:
        flash(result, 'warning')
    return redirect(url_for('read_recipes', category_title=session['active_category_title']))

@app.route('/load_details',methods=['GET'])
@login_required
def load_details():
    return render_template("table/details.html")


@app.route('/logout')
@login_required
def logout():
    """ logs out users """
    session.pop('username')
    flash('You have logged out', 'warning')
    return redirect(url_for('index'))
