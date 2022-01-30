from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Optional


class AddPet(FlaskForm):
    '''Form for creating pets'''

    name = StringField('Pet Name', validators=[InputRequired()])
    species = StringField('Species', validators=[InputRequired()])
    photo_url = StringField('Photo URL', validators=[Optional()])
    age = IntegerField('Age', validators=[Optional()])
    notes = StringField('Notes', validators=[Optional()])
    