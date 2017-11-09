from app import app
from flask import Flask, request, session, g, redirect, url_for, abort,render_template, flash, _app_ctx_stack
from src.modals import User, Category, Recipe
users_db = {}
app.secret_key = 'ggtsha6667jshjhsaknks9'

@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        if request.form['username'] in users_db:
            if request.form['password'] == users_db[request.form['username']].password:
                session['active_user']=request.form['username']
                session['login_in']=True
                
                return redirect(url_for('read_categories'));
            else:
                return redirect(url_for('login'))
        else:
            return redirect(url_for('register'))
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        if request.form['password']==request.form['rpt_password']:
            users_db[request.form['username']]=User(request.form['name'],request.form['username'],request.form['password'])
            return redirect('/login')
        else:
            return 'Passwords dont match'
    else:
        return render_template('register.html')

@app.route('/categories', methods=['GET','POST'])
@app.route('/categories/<active_category>', methods=['GET','POST'])
def read_categories(active_category=None):
    if 'active_user' in session:
        if request.method=='POST':
            if request.form['submit']=='Add':
                users_db[session['active_user']].add_category(Category(request.form['categoryname']))
                import pdb; pdb.set_trace()
            else:
                users_db[session['active_user']].get_categories()[request.form['categoryname']]=users_db[session['active_user']].get_categories().pop(active_category)
            return redirect('/categories')
        else:
            if not 'active_user' in session:
                return redirect('/login')
            else:
                return render_template('categories.html',category=active_category,categories=users_db[session['active_user']].get_categories())
    else:
        abort(403)
@app.route('/recipes/<categoryname>/<action>', methods=['GET','POST'])
def modify_lists(categoryname,action):
    if 'active_user' in session:
        if action=="delete":
            del users_db[session['active_user']].get_categories()[categoryname]
            return redirect('/categories')
        elif action=="edit":
            return redirect('/categories/'+categoryname)
    else:
        abort(403)
@app.route('/recipes/<categoryname>', methods=['GET','POST'])
@app.route('/recipes/<categoryname>/<recipename>', methods=['GET','POST'])
@app.route('/recipes/<categoryname>/<recipename>/<action>', methods=['GET','POST'])
def read_recipes(categoryname=None,recipename=None,action=None):
    if 'active_user' in session:
        if request.method=='POST':
            if request.form['submit']=='Add':
                users_db[session['active_user']].get_categories()[categoryname].add_recipe(Recipe(request.form['recipename']))
            else:
                users_db[session['active_user']].get_categories()[categoryname].get_recipes()[request.form['recipename']]=users_db[session['active_user']].get_categories()[categoryname].get_recipes().pop(recipename)
                users_db[session['active_user']].get_categories()[categoryname].get_recipes()[request.form['recipename']].status=request.form['status']
            return redirect('/recipes/'+categoryname)
        else:
            if not action is None:
                #return render_template('recipes.html',category=listname,recipes=users_db[session['active_user']].get_categories()[listname].get_recipes(),recipe=None)
                if action=='delete':
                    del users_db[session['active_user']].get_categories()[categoryname].get_recipes()[recipename]
                    return redirect('/recipes/'+categoryname)
                elif action=='edit':
                    #return redirect('/recipes/'+listname+'/'+recipename)
                    return render_template('recipes.html',category=categoryname,recipes=users_db[session['active_user']].get_categories()[categoryname].get_recipes(),recipe=recipename)
                else:
                    return redirect('/recipes/'+categoryname)
            else:
                return render_template('recipes.html',category=categoryname,recipes=users_db[session['active_user']].get_categories()[categoryname].get_recipes(),recipe=recipename)
    else:
        abort(403)
@app.route('/logout', methods=['GET','POST'])
def logout():
    if 'active_user' in session:
        session.pop('active_user',None)
    return redirect('/login')

@app.errorhandler(404)
def page_not_found(e):
    return '<h1>Error 404</h1><h3>Page does not exist on this Recipes  application</h3>'

@app.errorhandler(403)
def page_not_found(e):
    return '<h1>Error 403</h1><h3>You are not authorized to view this page</h3>'