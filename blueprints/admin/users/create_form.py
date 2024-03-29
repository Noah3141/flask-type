
from typing import Any
from typing_extensions import override
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, validators as v



class CreateUserForm(FlaskForm):
    name = StringField(
        "Name", 
        [v.DataRequired("Required!")],
        
    )
    nickname = StringField(
        "Nickame (Optional)",
        [],
    )
    age = IntegerField(
        "Age", 
        [v.InputRequired("is a required field")]
    )
    cool = BooleanField(
        "Cool", 
        default=False
    )

    
    submit = SubmitField("Submit")


