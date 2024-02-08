
from typing import Any
from typing_extensions import override
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, validators as v



class UpdateUserForm(FlaskForm):
    name = StringField(
        "Name", 
        [v.InputRequired()]
    )
    nickname = StringField(
        "Nickame (Optional)",
        default=None
    )
    age = IntegerField(
        "Age", 
        default=None
    )
    cool = BooleanField(
        "Cool", 
        default=False
    )

    
    submit = SubmitField("Submit")


