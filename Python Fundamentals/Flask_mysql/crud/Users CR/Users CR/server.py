from flask import Flask, render_template, request, redirect, session

# import the class from friend.py
from user import User
app = Flask(__name__)
app.secret_key = 'TheSosaGuwop'

# ! CREATE
@app.route('/results')
def results():
    return render_template("results.html", users = User.get_all())

@app.route('/results', methods = ["POST"])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/results')


# ! READ ALL
@app.route("/")
def index():
    return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True)

