# Import Flask to allow us to create our app
from flask import Flask, render_template, request, redirect, session

# Create a new instance of the Flask class called "app"
app = Flask(__name__) 
app.secret_key = 'TheSosaGuwop'

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')


@app.route('/show')
def show_user():
    return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])




# Ensure this file is being run directly and not from a different module
if __name__=="__main__":
    app.run(debug=True)    # Run the app in debug mode.

