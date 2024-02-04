
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class CreateOrganization(FlaskForm):
    name = StringField("Name")
    submit = SubmitField("Submit")