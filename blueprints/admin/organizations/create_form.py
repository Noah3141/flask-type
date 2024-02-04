
from typing import Any
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, validators as v

validators = [
    v.InputRequired("is a required field")
]

class CreateOrganizationForm(FlaskForm):
    pass

