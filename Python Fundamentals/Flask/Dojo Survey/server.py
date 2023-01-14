# Import Flask to allow us to create our app
from flask import Flask, render_template, request, redirect, session

# Create a new instance of the Flask class called "app"
app = Flask(__name__) 
app.secret_key = 'TheSosaGuwop'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/enter', methods=['POST'])
def enter():
    session['Your Name'] = request.form['Your Name']
    session['Dojo Location'] = request.form['Dojo Location']
    session['Favorite Language'] = request.form['Favorite Language']
    session['Comment'] = request.form['Comment']
    print(request.form)
    return redirect('/results')

@app.route('/results')
def results():
    return render_template("results.html")



# Ensure this file is being run directly and not from a different module
if __name__=="__main__":
    app.run(debug=True)    # Run the app in debug mode.

