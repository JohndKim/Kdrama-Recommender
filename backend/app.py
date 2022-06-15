from flask import Flask, jsonify, render_template, request

from rec_sys import get_titles, get_top_rec_kdrama

app = Flask(__name__)

# defines a route for "/"
# app.route a decorator: a special type of function that modifies another function
@app.route('/')
def index():
    return render_template('index.html', titles=get_titles())

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route("/about_me")
def about_me():
    return render_template('about_me.html')

@app.route('/click_me')
def click_me():
    return render_template('click_me.html')

@app.route('/search')
def search():
    # e.g. "Move to Heaven"
    # user_input = request.form('input')
    user_input = request.args.get("input")
    recommended_list = get_top_rec_kdrama(user_input)
    # check if title is in list of kdramas we have
    return render_template("search.html", titles=get_titles(), title=user_input, rec_list=recommended_list)




# runs this app
if __name__ == "__main__":
    app.run(debug=True)
