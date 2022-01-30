from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange, URL


class PetForm(FlaskForm):
    '''Form for creating pets'''

    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField('Species', choices=['dog', 'cat', 'porcupine'], 
                            validators=[InputRequired()])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(0, 30)])
    notes = StringField('Notes', validators=[Optional()])
