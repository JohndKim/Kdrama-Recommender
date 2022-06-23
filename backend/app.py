from datetime import timedelta

from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy

from rec_sys import (get_desc_word_count, get_info, get_titles,
                     get_top_rec_kdrama, kdrama_exists)

titles = get_titles()

app = Flask(__name__)
app.secret_key = "some_secret_key"
app.permanent_session_lifetime = timedelta(minutes=5)
# users = name of the table we're using
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:PA55word@127.0.0.1:3306/kdrama_users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

string = "\@"
db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(100))
    password = db.Column("password", db.String(100))
    email = db.Column("email", db.String(100))

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'P@55word'
# app.config['MYSQL_DB'] = 'kdrama_users'

# mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html', titles=titles)

@app.route('/help')
def help():
    return render_template('help.html')

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())

@app.route('/login', methods=['GET', 'POST'])
def login():
    # if login info entered
    if request.method == 'POST':
        session.permanent = True
        username = request.form["username"]
        password = request.form["password"]

        # cursor = mysql.connection.cursor()
        # cursor.execute("INSERT INTO users(username, password) VALUES(%s, %s)", (username, password))
        # mysql.connection.commit()
        # cursor.close()

        found_user = users.query.filter_by(username=username).first()
        # if user exists
        if found_user:
            # check if username matches password
            if found_user.password != password:
                flash("Incorrect username or password")
                return redirect(url_for("login"))
            
            session["username"] = username
            session["password"] = password
            session["email"] = found_user.email
        # else create return to login
        else:
            flash("Incorrect username or password")
            return redirect(url_for("login"))

        flash("Login Successful!")
        return redirect(url_for("profile"))
    
    # when accessing page
    else: 
        # if already logged in, go to profile page
        if "username" in session:
            flash("Already Logged In!", "info")
            return redirect(url_for("profile"))
        # else login page loaded
        return render_template("login.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    # if user info entered
    if request.method == 'POST':
        session.permanent = True

        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]

        found_email = users.query.filter_by(email=email).first()
        found_user = users.query.filter_by(username=username).first()
        # if username already exists, redirect + flash message user exists
        if found_user or found_email:

            flash("Username/Email already exists")
            return redirect(url_for("signup"))
        # else create new user
        else:
            usr = users(username, password, email)
            db.session.add(usr)
            db.session.commit()

        session["email"] = email
        session["username"] = username
        session["password"] = password

        flash("Signup Successful!")
        return redirect(url_for("profile"))
    
    # when accessing page
    else: 
        # if already logged in, go to profile page
        if "username" in session:
            flash("Already Logged In!", "info")
            return redirect(url_for("profile"))
        # else login page loaded
        return render_template("signup.html")


@app.route("/profile", methods=["POST", "GET"])
def profile():
    email = None

    # if logged in
    if "username" in session:
        username = session["username"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email

            # change current user's email
            found_user = users.query.filter_by(username=username).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved!")

        else: 
            if "email" in session:
                email = session["email"]

        return render_template("profile.html", username=username, email=email)
    # else redirect to login page
    else:
        flash("You are not logged in!", "info")
        return redirect(url_for("login"))

    # error = None
    # if request.method == 'POST':
    #     if request.form['username'] != 'admin' or request.form['password'] != 'admin': 
    #         error = 'Incorrect username or password.'
    #     else:
    #         return redirect(url_for('home'))
    # return render_template('login.html', error=error)

@app.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("password", None)
    session.pop("email", None)
    flash("You have been logged out!", "info")
    return redirect(url_for("login"))


@app.route('/settings')
def settings():
    global sort_by
    sort_by = request.args.get('sort')
    return render_template('settings.html')

@app.route("/about_me")
def about_me():
    return render_template('about_me.html')

@app.route('/click_me')
def click_me():
    return render_template('click_me.html')

@app.route('/search', methods=["POST", "GET"])
def search():
    if request.method == "GET":
        user_input = request.args.get("input")
        sort_by = request.args.get("sort")
        rec_num = request.args.get("num")

        # checks if title is valid
        if kdrama_exists(user_input, titles) == False:
            return render_template('error.html', error="The kdrama you have entered does not exist 😤")
        
        recommended_list = get_top_rec_kdrama(user_input, sort_by, rec_num)

        # recommended_list = {'link': {0: 'https://mydramalist.com/951-3-leaf-clover', 1: 'https://mydramalist.com/59381-navillera', 2: 'https://mydramalist.com/7184-good-doctor', 3: 'https://mydramalist.com/17315-rickety-rackety-family', 4: 'https://mydramalist.com/30917-dazzling', 5: 'https://mydramalist.com/60409-uncle', 6: 'https://mydramalist.com/4518-panda-and-hedgehog', 7: 'https://mydramalist.com/9162-pluto-squad', 8: 'https://mydramalist.com/2822-air-city'}, 'title': {0: '3 Leaf Clover', 1: 'Navillera', 2: 'Good Doctor', 3: 'Rickety Rackety Family', 4: 'The Light in Your Eyes', 5: 'Uncle', 6: 'Panda and Hedgehog', 7: 'Pluto Squad', 8: 'Air City'}, 'rank': {0: 2272, 1: 13, 2: 176, 3: 2579, 4: 277, 5: 329, 6: 1165, 7: 1596, 8: 1233}, 'score': {0: 7.0, 1: 9.0, 2: 8.3, 3: 4.8, 4: 8.2, 5: 8.1, 6: 7.2, 7: 7.6, 8: 7.1}, 'sim_score': {0: 37.3, 1: 33.9, 2: 30.7, 3: 27.4, 4: 27.3, 5: 24.4, 6: 22.7, 7: 8.7, 8: 8.5}}
        return render_template("search.html", titles=get_titles(), title=user_input, rec_list=recommended_list)

@app.route('/search_info')
def search_info():
    return render_template('search_info.html', titles=titles)

@app.route('/info')
def info():
    # check if "input" exists
    user_input = request.args.get("input")
    if kdrama_exists(user_input, titles) == False:
        return render_template('error.html', error="The kdrama you have entered does not exist 😤")

    info = get_info(user_input)

    desc = info['description']
    word_count = get_desc_word_count(desc)

    return render_template('info.html', info=info, word_count=word_count)
    # get info on kdrama with this (input) title



# runs this app
if __name__ == "__main__":
    db.create_all()
    db.session.commit()
    app.run(debug=True)
