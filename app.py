import os
from flask import Flask, render_template, redirect, request, url_for, session,flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
import bcrypt

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'myCookingDB'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
app.secret_key = "some_secret"

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        # try and get one with same name as entered
        db_user = users.find_one({'user_name': request.form['user_name']})

        if db_user:
            # check password using hashing
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'),
                             db_user['password']) == db_user['password']:
                session['user_name'] = request.form['user_name']
                session['logged_in'] = True
                # successful redirect to home logged in
                return redirect(url_for('index'))
            # must have failed set flash message
            flash('Invalid username/password combination')
    return render_template("login.html")

@app.route('/logout')
def logout():
    """Clears session and redirects to home"""
    session.clear()
    return redirect(url_for('index'))
    
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'user_name' : request.form['user_name']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one(
              { 'user_name' : request.form.get('user_name'), 'password' : hashpass, 'email' : request.form.get('email') })
            session['user_name'] = request.form['user_name']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')
    
@app.route('/get_recipes')
def get_recipes():
    return render_template('allergens.html',
                    recipes=mongo.db.recipes.find())
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                    allergens=mongo.db.allergens.find(),
                    cuisines=mongo.db.cuisines.find())

                            
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes=mongo.db.recipes
    recipes.insert_one({
        'recipe_name':request.form['recipe_name'],
        'short_description':request.form['short_description'],
        'cuisine_name':request.form['cuisine_name'],
        'allergen_name':request.form['allergen_name'],
        'cooking_time':request.form['cooking_time'],
        'prep_time':request.form['prep_time'],
        'serves':request.form['serves'],
        'image_link': request.form['image_link'],
        'ingredients':request.form['ingredients'],
        'method':request.form['method'],
        'views': 0,
        'user_name':session['user_name']
    })
    return redirect(url_for('get_recipes'))
    
if __name__=='__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)