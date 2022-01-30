from secret import SECRET_STRING
from flask import Flask, render_template, redirect
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension

from forms import PetForm

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


@app.route("/add", methods=['GET', 'POST'])
def add_pet():
    petform = PetForm()

    if petform.validate_on_submit():
        new_pet = Pet(name=petform.name.data, 
                      species=petform.name.data,
                      photo_url=petform.photo_url.data,
                      age=petform.age.data,
                      notes=petform.notes.data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add.html', form=petform)


@app.route("/<int:pet_id>", methods=['GET', 'POST'])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    edit_form = PetForm(obj=pet)

    if edit_form.validate_on_submit():
        pet.name = edit_form.name.data
        pet.species = edit_form.species.data
        pet.photo_url = edit_form.photo_url.data
        pet.age = edit_form.age.data
        pet.notes = edit_form.notes.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit.html', form=edit_form)

