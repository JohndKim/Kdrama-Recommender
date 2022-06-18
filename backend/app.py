from flask import Flask, jsonify, render_template, request

from rec_sys import get_info, get_titles, get_top_rec_kdrama, kdrama_exists

titles = get_titles()

app = Flask(__name__)

# defines a route for "/"
# app.route a decorator: a special type of function that modifies another function
@app.route('/')
def index():
    return render_template('index.html', titles=titles)

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
    user_input = request.args.get("input")
    # checks if title is valid
    if kdrama_exists(user_input, titles) == False:
        return render_template('error.html', error="The kdrama you have entered does not exist 😤")
    # recommended_list = get_top_rec_kdrama(user_input, "sim score")

    recommended_list = {'link': {0: 'https://mydramalist.com/951-3-leaf-clover', 1: 'https://mydramalist.com/59381-navillera', 2: 'https://mydramalist.com/7184-good-doctor', 3: 'https://mydramalist.com/17315-rickety-rackety-family', 4: 'https://mydramalist.com/30917-dazzling', 5: 'https://mydramalist.com/60409-uncle', 6: 'https://mydramalist.com/4518-panda-and-hedgehog', 7: 'https://mydramalist.com/9162-pluto-squad', 8: 'https://mydramalist.com/2822-air-city'}, 'title': {0: '3 Leaf Clover', 1: 'Navillera', 2: 'Good Doctor', 3: 'Rickety Rackety Family', 4: 'The Light in Your Eyes', 5: 'Uncle', 6: 'Panda and Hedgehog', 7: 'Pluto Squad', 8: 'Air City'}, 'rank': {0: 2272, 1: 13, 2: 176, 3: 2579, 4: 277, 5: 329, 6: 1165, 7: 1596, 8: 1233}, 'score': {0: 7.0, 1: 9.0, 2: 8.3, 3: 4.8, 4: 8.2, 5: 8.1, 6: 7.2, 7: 7.6, 8: 7.1}, 'sim_score': {0: 37.3, 1: 33.9, 2: 30.7, 3: 27.4, 4: 27.3, 5: 24.4, 6: 22.7, 7: 8.7, 8: 8.5}}
    return render_template("search.html", titles=get_titles(), title=user_input, rec_list=recommended_list)

@app.route('/info')
def info():
    # check if "input" exists
    user_input = request.args.get("input")
    if kdrama_exists(user_input, titles) == False:
        return render_template('error.html', error="The kdrama you have entered does not exist 😤")

    info = get_info(user_input)
    return render_template('info.html', info=info)
    # get info on kdrama with this (input) title


# runs this app
if __name__ == "__main__":
    app.run(debug=True)
