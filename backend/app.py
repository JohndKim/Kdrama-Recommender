from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# looks for "index.html" in the templates folder
# ('/') is the path IDKKKK
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template()
    # # GET request
    # if request.method == 'GET':

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

# runs this app
if __name__ == "__main__":
    app.run(debug=True)
