
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, validators as v


class CreateUserForm(FlaskForm):
    name = StringField(
        "Name", 
        [v.DataRequired("Required!")],
    )
    nickname = StringField(
        "Nickame (Optional)",
        []
    )
    age = IntegerField(
        "Age", 
        [v.InputRequired("is a required field")]
    )
    cool = BooleanField(
        "Cool", 
        [v.InputRequired("is a required field")], 
        default=False
    )

    submit = SubmitField("Submit")

