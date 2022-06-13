from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# defines a route for "/"
# app.route a decorator: a special type of function that modifies another function
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/about_me")
def about_me():
    return render_template('about_me.html')

@app.route('/search', methods=["GET", "POST"])
def search():
    return render_template("search.html")
    # # GET request
    # if request.method == 'GET':



# runs this app
if __name__ == "__main__":
    app.run(debug=True)
