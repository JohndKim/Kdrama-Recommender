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
    # recommended_list = get_top_rec_kdrama(user_input)

    recommended_list = {'title': {0: '3 Leaf Clover', 1: 'Navillera', 2: 'Good Doctor', 3: 'Rickety Rackety Family', 4: 'The Light in Your Eyes', 5: 'Uncle', 6: 'Panda and Hedgehog', 7: 'Pluto Squad', 8: 'Air City'}, 'rank': {0: 2272, 1: 13, 2: 176, 3: 2579, 4: 277, 5: 329, 6: 1165, 7: 1596, 8: 1233}, 'score': {0: 7.0, 1: 9.0, 2: 8.3, 3: 4.8, 4: 8.2, 5: 8.1, 6: 7.2, 7: 7.6, 8: 7.1}, 'sim_score': {0: 37.3, 1: 33.9, 2: 30.7, 3: 27.4, 4: 27.3, 5: 24.4, 6: 22.7, 7: 8.7, 8: 8.5}}

    # check if title is in list of kdramas we have
    return render_template("search.html", titles=get_titles(), title=user_input, rec_list=recommended_list)




# runs this app
if __name__ == "__main__":
    app.run(debug=True)
