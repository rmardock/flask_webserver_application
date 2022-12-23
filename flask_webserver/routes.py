from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

# Import modules here
from .forms import *
from .db_connection_utility import *

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("landing.html")

@app.route("/login", methods=['GET', 'POST'])
def login_page():
    # Initialize variables
    validation_error = None
    form = LoginForm()
    if(request.method == 'POST' and form.validate_on_submit()):
        # Get username and password from form
        username = request.form['username']
        password = request.form['password']
        # Create flask session here to pass username
        # Query database to check inputted user credentials
        if(query_db(username, password) == True):
            # If credentials are validated, redirect to admin page
            validation_error = None
            return redirect('/admin')
        else:
            validation_error = "Incorrect username or password! Please try again."
        
    return render_template("login.html", form=form, validation_error=validation_error)

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    return render_template("admin.html")