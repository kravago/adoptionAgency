from secret import SECRET_STRING
from flask import Flask, render_template
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_STRING

# sqlalchemy settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


# Toolbar stuff
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


# init db connection
connect_db(app)


# routes
@app.route("/")
def homepage():
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)